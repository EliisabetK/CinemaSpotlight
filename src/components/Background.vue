<template>
    <div class="video-background">
      <video id="vid" playsinline autoplay muted loop>
        <source src="@/assets/background.mp4" type="video/mp4">
      </video>
      <slot></slot> <!-- This is where the content of the parent component will be injected -->
    </div>
  </template>
  
  <script>
  export default {
    name: 'VideoBackground',
    mounted() {
      var video = document.getElementById('vid');
      if (video) {
        video.playbackRate = 0.5;
      }
    },
  };
  </script>
  
  <style>
  .video-background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
  }
  
  .video-background video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -1;
  }
  </style>
  