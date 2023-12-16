<template>
  <router-link :to="'/singlepost/' + id">
    <div id="postDiv" ref="dynamicContent">
      <div class="post">
        <div class="post-header">
          <p class="post-date">{{ getDate(post_date) }}</p>
        </div>
        <p class="post-content">{{ post_text }}</p>
      </div>
    </div>
  </router-link>
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
    getDate(dateString) {
      const postDate = new Date(dateString);
      const currentDate = new Date();
      const timeDifference = currentDate - postDate;

      if (timeDifference < 60 * 60 * 1000) {
        const minutesAgo = Math.floor(timeDifference / (60 * 1000));
        return `${minutesAgo} minutes ago`;
      } else if (timeDifference < 24 * 60 * 60 * 1000) {
        const hoursAgo = Math.floor(timeDifference / (60 * 60 * 1000));
        return `${hoursAgo} hours ago`;
      } else {
        const months = [
          'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
        ];
        const month = months[postDate.getMonth()];
        const date = postDate.getDate();
        const year = postDate.getFullYear();
        return `${month} ${date}, ${year}`;
      }
    }
  }
};
</script>

<style scoped>
.post {
  background-color: rgb(186, 202, 210);
  border-radius: 10px;
  padding: 1em;
  margin-bottom: 1em;
  word-wrap: break-word;
}
.post p {
  font-size: 1.5em;
  color: #1e2b21;
  margin-bottom: 0.5em;
}
.post-header {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 0.5em;
}

.post-header p {
  margin-bottom: 0.5em;
  font-size: 1.3em;
  color: #28352b;
}

@media (max-width: 600px) {
  .post p {
    font-size: 0.9em;
    margin-bottom: 0.25em;
  }
}
</style>
