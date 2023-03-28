<template>
  <div>
    <div class="channels-card-image-btn">
      <button type="button" class="btn btn-outline-danger btn-sm" v-on:click="onRecognitionStart">Включить голосовое управление</button>
    </div>
    <video ref="videoPlayer"
           class="video-js"
           width="1080">

    </video>
    <audio ref="audioPlayerRef" id="player"></audio>
  </div>
</template>

<script lang="ts">
import { Ref } from 'vue-property-decorator';
import { Options, Vue } from 'vue-class-component';

import videojs from 'video.js';
import Subtitle from '@/models/Subtitle';
import utils from '@/services/utils';

// const SpeechRecognition = window.SpeechRecognition || webkitSpeechRecognition;

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

  audioPlayerRef!: any;

  timeDict: { [index: number]: number } = {};

  audioDict: { [index: string]: any } = {};

  timer!: number | null;

  recognition: any;

  @Ref('videoPlayer') readonly videoPlayer!: HTMLVideoElement

  @Ref('audioPlayerRef') readonly audioPlayer!: HTMLAudioElement

  mounted() {
    this.initSpeachRecognition();

    for (let i = 0; i < this.subtitles.length; i++) {
      const subtitle = this.subtitles[i];
      const startSecond = utils.frameToSeconds(subtitle.startFrame, this.fps);
      this.timeDict[startSecond] = i;
      if (subtitle.voiceFilePath) {
        const audioFile = utils.getUrl(subtitle.voiceFilePath);
        const audio = new Audio(audioFile);
        audio.preload = 'auto';
        audio.addEventListener('canplaythrough', this.loadedAudio, false);
        this.audioDict[subtitle.voiceFilePath] = audio;
      }
    }

    this.player = videojs(this.videoPlayer, this.options, () => {
      this.player.log('onPlayerReady', this);
    });

    this.player.on('loadedmetadata', this.onLoadedMetadata);
    this.player.on('timeupdate', this.onTimeUpdate);
  }

  initSpeachRecognition() {
    // const TsSpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
    // const speechRecognitionEvent = SpeechRecognitionEvent || webkitSpeechRecognitionEvent;
    // eslint-disable-next-line new-cap
    this.recognition = new webkitSpeechRecognition();
    this.recognition.continuous = true;
    this.recognition.lang = 'ru-RU';
    this.recognition.interimResults = false;
    this.recognition.maxAlternatives = 1;

    this.recognition.onresult = this.onRecognitionEvent;
    this.recognition.onspeechend = this.onSpeechEnd;
    this.recognition.onnomatch = this.onNoMatch;
    this.recognition.onerror = this.onRecognitionError;
  }

  onRecognitionStart(event: SpeechRecognitionEvent) {
    this.recognition.start();
  }

  onRecognitionEvent(event: any) {
    // The SpeechRecognitionEvent results property returns a SpeechRecognitionResultList object
    // The SpeechRecognitionResultList object contains SpeechRecognitionResult objects.
    // It has a getter so it can be accessed like an array
    // The first [0] returns the SpeechRecognitionResult at the last position.
    // Each SpeechRecognitionResult object contains SpeechRecognitionAlternative objects that contain individual results.
    // These also have getters so they can be accessed like arrays.
    // The second [0] returns the SpeechRecognitionAlternative at position 0.
    // We then return the transcript property of the SpeechRecognitionAlternative object
    const command = event.results[event.results.length - 1][0].transcript.trim().toLowerCase();
    if (command === 'старт') {
      this.player.play();
    } else if (command === 'стоп') {
      this.player.pause();
    }
  }

  onSpeechEnd() {
    console.log('Speech end');
  }

  onNoMatch(event: any) {
    console.log('I didn\'t recognise command');
  }

  onRecognitionError(event: any) {
    console.log(`Error occurred in recognition: ${event.error}`);
  }

  loadedAudio(event: any) {
    // console.log(event);
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
        this.player.currentTime(markerTime);
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
      const durationSecond = utils.frameToSeconds(subtitle.endFrame - subtitle.startFrame, this.fps);
      // console.log(subtitle.voiceFilePath);
      if (subtitle.voiceFilePath != null) {
        const audio = this.audioDict[subtitle.voiceFilePath];
        audio.play();
        // this.audioPlayer.src = this.audioDict[subtitle.voiceFilePath];
        // this.audioPlayer.play();
      }

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
