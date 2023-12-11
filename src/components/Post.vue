<!-- veel ei tööta aga baas olemas -->

<template>
  <div id="postDiv" ref="dynamicContent">
    <div class="post">
      <div class="post-header">
        <p class="post-date">{{ getDate(post_date) }}</p>
      </div>
      <p class="post-content">{{ post_text }}</p>
    </div>
  </div>
</template>
 
<script>
export default {
  name: 'Post',
  props: ['id', 'post_date', 'post_text'],
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
    getDate(dateString) {
      const postDate = new Date(dateString);
      const months = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
      ];
      const month = months[postDate.getMonth()];
      const date = postDate.getDate();
      const year = postDate.getFullYear();
      const dateStringNew = `${month} ${date}, ${year}`
      return dateStringNew;
    }
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

.post p{
  font-size: 1.5em;
  color: #1e2b21;
  margin-bottom: 0.5em; 
}

.image-container {
  margin-bottom: 1em; 
}

.post-image {
  width: 50%;
  height: auto;
  border-radius: 8px;
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
