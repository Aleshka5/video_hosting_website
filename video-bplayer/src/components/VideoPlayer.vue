<template>
  <div>
    <video ref="videoPlayer"
      class="video-js"
      controls
      preload="auto"
      width="1080">
      <source src="@/assets/video/kamila.mp4" type="video/mp4" />
    </video>
  </div>
</template>

<script lang="ts">
import { Ref } from 'vue-property-decorator';
import { Options, Vue } from 'vue-class-component';

import videojs from 'video.js';

@Options({
  props: {
    options: Object,
  },
})
export default class VideoPlayer extends Vue {
  options!: object;

  player!: any;

  markers = [
    { time: 20, label: 'Romance', audio: 'romance.ogg' },
    { time: 40, label: 'collect', audio: 'collect.ogg' },
    { time: 50, label: 'exclude', audio: 'exclude.ogg' },
    { time: 80, label: 'accord', audio: 'accord.ogg' },
  ];

  timeDict: {[index: number]: number} = {};

  timer!: number | null;

  @Ref('videoPlayer') readonly videoPlayer!: HTMLVideoElement

  mounted() {
    for (let i = 0; i < this.markers.length; i++) {
      this.timeDict[this.markers[i].time - 1] = i;
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

    for (let i = 0; i < this.markers.length; i++) {
      const left = `${((this.markers[i].time / total) * 100)}%`;
      const markerTime = this.markers[i].time;

      const newDiv = document.createElement('div');
      newDiv.className = 'vjs-marker';
      newDiv.style.left = left;
      const newSpan = document.createElement('span');
      const newContent = document.createTextNode(this.markers[i].label);

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
      const audioFile = this.markers[markerIndex].audio;
      console.log(audioFile);
      const someSound = require(`../assets/audio/${audioFile}`);
      const audio = new Audio(someSound);
      audio.play();

      this.timer = setTimeout(() => {
        this.timer = null;
        this.player.volume(currentVolume);
      }, 1200);
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
