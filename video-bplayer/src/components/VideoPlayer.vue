<template>
  <div>
    <video ref="videoPlayer"
           class="video-js"
           width="1080">

    </video>
  </div>
</template>

<script lang="ts">
import { Ref } from 'vue-property-decorator';
import { Options, Vue } from 'vue-class-component';

import videojs from 'video.js';
import Subtitle from '@/models/Subtitle';
import utils from '@/services/utils';

@Options({
  props: {
    fps: Number,
    subtitles: Array,
    options: Object,
  },
})
export default class VideoPlayer extends Vue {
  fps!: number;

  options!: object;

  subtitles!: Subtitle[];

  player!: any;

  timeDict: { [index: number]: number } = {};

  timer!: number | null;

  @Ref('videoPlayer') readonly videoPlayer!: HTMLVideoElement

  mounted() {
    for (let i = 0; i < this.subtitles.length; i++) {
      const startSecond = utils.frameToSeconds(this.subtitles[i].startFrame, this.fps);
      this.timeDict[startSecond - 1] = i;
    }

    this.player = videojs(this.videoPlayer, this.options, () => {
      this.player.log('onPlayerReady', this);
    });

    this.player.on('loadedmetadata', this.onLoadedMetadata);
    this.player.on('timeupdate', this.onTimeUpdate);
  }

  onLoadedMetadata() {
    const total = this.player.duration();

    const p = this.player.controlBar.progressControl.children_[0].el_;

    console.log(p);

    for (let i = 0; i < this.subtitles.length; i++) {
      const startSecond = utils.frameToSeconds(this.subtitles[i].startFrame, this.fps);
      const left = `${((startSecond / total) * 100)}%`;
      const markerTime = startSecond;

      const newDiv = document.createElement('div');
      newDiv.className = 'vjs-marker';
      newDiv.style.left = left;
      const newSpan = document.createElement('span');
      const newContent = document.createTextNode(this.subtitles[i].textSubtitle);

      // add the text node to the newly created div
      newSpan.appendChild(newContent);
      newDiv.appendChild(newSpan);
      newDiv.addEventListener('click', () => {
        this.player.currentTime(markerTime - 1);
      });

      p.appendChild(newDiv);
    }
  }

  onTimeUpdate(event: any) {
    const currentTime = Math.round(this.player.currentTime());

    if (currentTime in this.timeDict && this.timer == null) {
      console.log(this.player.currentTime());
      console.log(currentTime);
      const currentVolume = this.player.volume();
      this.player.volume(0.1);
      const markerIndex = this.timeDict[currentTime];
      const subtitle = this.subtitles[markerIndex];
      const audioFile = utils.getUrl(subtitle.voiceFilePath);
      // console.log(audioFile);
      // const someSound = require(`../assets/audio/${audioFile}`);
      const durationSecond = utils.frameToSeconds(subtitle.endFrame - subtitle.startFrame, this.fps);
      const audio = new Audio(audioFile);
      audio.play();

      this.timer = setTimeout(() => {
        this.timer = null;
        this.player.volume(currentVolume);
      }, durationSecond * 1000);
    }
  }

  beforeDestroy() {
    if (this.player) {
      this.player.dispose();
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
</style>
