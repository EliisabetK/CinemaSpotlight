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
.resetLikesButton > button:hover{
  background-color: rgb(160, 197, 235);
}
.resetLikesButton > button:active{
  padding: 0.53em;
}
.resetLikesButton > button{
  display: flex;
  margin: 0.25em;
  padding: 0.5em;
  background-color: #85abc4;
  border: none;
  border-radius: 10%;
  font-size: 1em;
  color: rgb(24, 31, 31);
}
.container {
    display: flex;
    /*min-height: calc(100vh - 4.5em);*/
    max-height: calc(100vh - 6.5em);
    column-gap: 3em;
  }
  
  .left-column, .right-column {
    flex: 1;
    background-color: #7597ad;
    border-radius: 10px;
    margin-top: 5em;
    position: sticky;
    z-index: -1;
  }
  
  main {
    margin-top: 5em;
    flex: 3; 
    overflow-y: auto; 
    max-height: calc(100vh - 10em); 
  }
</style>