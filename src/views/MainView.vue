<template>
  <div>
    <div class="container">
      <aside class="left-column"></aside>

      <main>
        <div>
          <Post
          v-for="post in postList"
           :id="post.id"
           :post_date= "post.date"
           :post_text= "post.text"
           :creator_name= "post.creator_name"
           :image_url= "post.image_url"
           :like_count= "post.likeCount"
        />
        </div>
      </main>
      <aside class="right-column"></aside>
    </div>
    <div class="resetLikesButton">
      <button v-on:click="resetLikeCount">Reset likes</button>
    </div>
  </div>
</template>

<script>
import Post from '@/components/Post.vue'

console.log("mainView script started and Post imported")
export default {
    name: "MainView",
    data: function() {
      return {
      }
    }, 
    computed: {
      postList() {
        return this.$store.state.postList;
      }
    },
    components: {
      Post,
    },
    methods:{
      resetLikeCount: function(){
        this.$store.commit("resetLikeCount");
      }
    }
}
//console.log("postList found??", postList[0].text)
// formats the date to be in the style of "Oct 4, 2023"


</script>

<style>
.resetLikesButton{
  display: flex;
  justify-content: center;
}
button{
  display: flex;
  margin: 0.5em;
  padding: 0.5em;
  border-radius: 5px;
}
</style>