<template>
  <div class="container-fluid pb-0">
    <div class="video-block section-padding">
      <div class="row">
        <div class="col-md-8">
          <div class="single-video-left">
            <div v-if="!videoOptions">
              Загрузка...
            </div>
            <div v-if="videoOptions" class="single-video">
              <VideoPlayer :options="videoOptions" :subtitles="subtitles" :fps="fps"/>
            </div>
            <div class="single-video-title box mb-3">
              <h2>{{ video?.videoName }}</h2>
            </div>

            <div class="single-video-info-content box mb-3">
              <h6>Категория :</h6>
              <p>{{ video?.videoCategory }}</p>
              <h6>Описание :</h6>
              <p>{{ video?.videoDescription }}</p>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="single-video-right">
            <div class="row" v-if="video">
              <div class="col-md-12">
                <h5>Аннотации:</h5>
              </div>
              <div class="col-md-12" v-for="subtitle in subtitles" :key="subtitle.id">
                <div class="video-card video-card-list">
                  <div class="video-card-body">
                    <div class="video-title">
                      <span class="time-s">{{ $utils.durationToString($utils.frameToSeconds(subtitle.startFrame, this.fps)) }}</span> <b>{{ subtitle.textSubtitle }}</b>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import VideoPlayer from '@/components/VideoPlayer.vue';
import { getSubtitlesByVideo, getVideoById } from '@/services/api-service';
import Video from '@/models/Video';
import utils from '@/services/utils';
import Subtitle from '@/models/Subtitle';

@Options({
  components: {
    VideoPlayer,
  },
})
export default class VideoView extends Vue {
  videoOptions: any = null;

  video: Video | null = null;

  fps = 0;

  subtitles: Subtitle[] = [];

  compareSubtitles(subtitle1: Subtitle, subtitle2: Subtitle) {
    if (subtitle1.startFrame >= subtitle2.startFrame) {
      return 1;
    }
    return -1;
  }

  async mounted(): Promise<void> {
    const id = this.$route.params.id as string;
    const videoId = parseInt(id, 10);
    this.video = await getVideoById(videoId);
    this.fps = this.video.fps;
    this.subtitles = await getSubtitlesByVideo(videoId);
    this.subtitles = this.subtitles.sort(this.compareSubtitles);
    this.videoOptions = {
      autoplay: false,
      controls: true,
      fluid: true,
      poster: utils.getUrl(this.video.videoPreviewPath),
      sources: [{
        src: utils.getUrl(this.video.videoFilePath),
        type: 'video/mp4',
      }],
    };
  }
}
</script>
