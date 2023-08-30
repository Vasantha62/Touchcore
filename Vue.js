<template>
  <div>
    <input type="file" @change="https://www.youtube.com/watch?v=YehYUawzTl0" />
    <video ref="videoRef">
      <track v-for="(subtitle, index) in subtitles" :key="index" :src="subtitle.src" :label="subtitle.label" default />
    </video>
    <div v-for="(subtitle, index) in subtitles" :key="index" class="subtitle-box">
      <input v-model="subtitle.text" @input="updateSubtitle(index)" />
    </div>
    <button @click="playVideo">Play</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      videoFile: null,
      subtitles: [],
      videoElement: null,
    };
  },
  methods: {
    handleFileUpload(event) {
      this.videoFile = event.target.files[0];
      // Create track elements for subtitles
      // Initialize subtitles array with timestamps and text
    },
    updateSubtitle(index) {
      // Update the subtitle text in the subtitles array
    },
    playVideo() {
      // Play the video
    },
  },
  mounted() {
    this.videoElement = this.$refs.videoRef;
  },
};
</script>

<style>
.subtitle-box {
  margin-top: 10px;
}
</style>

