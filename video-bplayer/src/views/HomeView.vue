<template>
  <div class="container-fluid pb-0">
    <div class="top-mobile-search">
      <div class="row">
        <div class="col-md-12">
          <form class="mobile-search">
            <div class="input-group">
              <input type="text" placeholder="Search for..." class="form-control">
              <div class="input-group-append">
                <button type="button" class="btn btn-dark"><i class="fas fa-search"></i></button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div class="video-block section-padding">
      <div class="row">
        <div class="col-md-12">
          <div class="main-title">
            <div class="btn-group float-right right-action">
            </div>
            <h6>Видеоролики</h6>
          </div>
        </div>
        <div class="col-xl-3 col-sm-6 mb-3" v-for="video in videos" :key="video.id">
          <div class="video-card">
            <div class="video-card-image">
              <a class="play-icon" :href="`/video/${video.id}`"><i class="fas fa-play-circle"></i></a>
              <a :href="`/video/${video.id}`"><img class="img-fluid" :src="$utils.getUrl(video.videoPreviewPath)" alt=""></a>
              <div class="time">{{ $utils.durationToString(video.durationSeconds) }}</div>
            </div>
            <div class="video-card-body">
              <div class="video-title">
                <a :href="`/video/${video.id}`">{{ video.videoName }}</a>
              </div>
              <div class="video-page text-success">
                {{ video.videoCategory }} <a title="" data-placement="top" data-toggle="tooltip" href="#"
                             data-original-title="Verified"><i
                class="fas fa-check-circle text-success"></i></a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <hr class="mt-0">
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import { getVideos } from '@/services/api-service';
import Video from '@/models/Video';

@Options({
  components: {},
})
export default class HomeView extends Vue {
  videos: Video[] = [];

  async mounted(): Promise<void> {
    this.videos = await getVideos();
  }
}
</script>
