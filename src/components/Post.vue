<template>
  <div id="postDiv" ref="dynamicContent">
    <div class="post">
      <div class="post-header">
        <div class="profile-image-and-username">
          <img :src="require('@/assets/icon.png')" alt="Profile Image" class="profile-image" />
          <span class="username">{{ creator_name }}</span>
        </div>
        <p class="post-date">{{ formatDate(post_date) }}</p>
      </div>
      <div v-if="image_url" class="image-container">
        <img :src="image_url" alt="Post Image" class="post-image" />
      </div>
      <p class="post-content">{{ post_text }}</p>
      <div class="like-container">
        <img
          src="@/assets/thumb.png"
          alt="Like Icon"
          class="like-image"
          @click="handleLikeClick"
        />
        <p class="like-count">Likes: {{ like_count }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Post',
  props: ['id', 'post_date', 'post_text', 'creator_name', 'image_url', 'like_count'],
  data() {
    return {
    };
  },
  methods: {
    formatDate(dateString) {
      const postDate = new Date(dateString);
      const currentDate = new Date();
      const timeDifference = currentDate - postDate;

      if (timeDifference < 24 * 60 * 60 * 1000) {
        const hoursAgo = Math.floor(timeDifference / (60 * 60 * 1000));
        return `${hoursAgo} hours ago`;
      } else {
        const options = { year: 'numeric', month: 'short', day: 'numeric' };
        return postDate.toLocaleDateString(undefined, options);
      }
    },
    handleLikeClick: function() {
      this.$store.commit("incrementLikeCount", this.id);
    },
  },
};
</script>

<style scoped>
.post {
  background-color: rgb(186, 202, 210);
  border-radius: 10px;
  padding: 1em;
  margin-bottom: 1em;
}

.post-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5em;
}

.profile-image {
  width: 40px;
  height: 40px;
  object-fit: cover;
  margin-bottom: 1em;
  margin-right: 1em;
}

.username {
  color: #293c2e;
  margin-top: -2.7em;
  margin-left: 3.3em;
  margin-bottom: 0.5em; 
  display: flex;
  align-items: center;
  font-size: 1.2em;
}

.post p{
  font-size: 1.5em;
  color: #1e2b21;
  margin-bottom: 0.5em; 
}

.profile-image-and-username + p {
  margin-top: 0.5em;
  color: #293c2e;
  font-size: 1.2em;
}

.image-container {
  margin-bottom: 1em; 
}

.post-image {
  width: 50%;
  height: auto;
  border-radius: 8px;
}

.like-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: -0.5em;
  margin-bottom: -0.5em;
}

.like-image {
  width: 40px;
  height: 40px;
  margin-right: 5px;
}
.like-image:active{
  width: 40.5px;
  height: 40.5px;
  margin-right: 5px;
}

.like-count {
  font-size: 1.5em;
  color: #293c2e;
}

@media (max-width: 600px) {
  .profile-image {
    width: 30px;
    height: 30px;
    object-fit: cover;
  }

  .post p {
    font-size: 0.9em;
    margin-bottom: 0.25em;
  }

  .username {
    font-size: 1em;
    margin-bottom: 0.25em;
  }
}
</style>
