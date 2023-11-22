
<template>
  <div>
    <div class="container">
      <aside class="left-column"></aside>

      <main>
        <div>
          <Post
          v-for="post in postList"
           :post_date= post.date
           :post_text= post.text
           :creator_name= post.creator_name
           :image_url= post.image_url
        />
        </div>
      </main>

      <aside class="right-column"></aside>
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
    }, computed: {
      postList() {
        return this.$store.state.postList;
    }
    },
    components: {
      Post: Post
    }
}
//console.log("postList found??", postList[0].text)
// formats the date to be in the style of "Oct 4, 2023"


</script>

<style>
</style>