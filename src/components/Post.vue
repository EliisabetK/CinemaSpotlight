<template>
  <div id="postDiv" ref="dynamicContent"></div>
</template>
  
  <script>
  let self = this;
  export default {
        name: 'Post',
        props: ['post_date','post_text','creator_name','image_url'],
        mounted(){
          function formatDate(dateString) {
                    const postDate = new Date(dateString);
                    const currentDate = new Date();
                    const timeDifference = currentDate - postDate;
                    
                    // if the post is less than a day old it shows how many hours ago it was created
                    if (timeDifference < 24 * 60 * 60 * 1000) {
                        const hoursAgo = Math.floor(timeDifference / (60 * 60 * 1000));
                        return `${hoursAgo} hours ago`;
                    } else {
                        const options = { year: 'numeric', month: 'short', day: 'numeric' };
                        return postDate.toLocaleDateString(undefined, options);
                    }
                }
                const postElement = document.createElement('div');
                postElement.classList.add('post');

                const postHeader = document.createElement('div');
                postHeader.classList.add('post-header');
                
                const profileImageAndUserName = document.createElement('div');

                // profile image
                const profileImage = document.createElement('img');
                profileImage.src = require('@/assets/icon.png'); // Use require to specify the image path
                profileImage.alt = "Profile Image";
                profileImage.classList.add('profile-image');
                profileImageAndUserName.append(profileImage);
                
                // username
                const userName = document.createElement('text');
                userName.textContent = this.creator_name;
                userName.classList.add('username');
                profileImageAndUserName.append(userName)

                postHeader.appendChild(profileImageAndUserName)

                // date
                const postDate = document.createElement('p');
                postDate.textContent = formatDate(this.post_date);
                postDate.classList.add('post-date');
                postHeader.appendChild(postDate);

                // add header to element
                postElement.appendChild(postHeader);

                // text
                const postContent = document.createElement('p');
                postContent.textContent = this.post_text;

                // image if it exists
                const imageContainer = document.createElement('div');
                const postImage = document.createElement('img');
                if (this.image_url) {
                    postImage.src = this.image_url;
                    postImage.alt = "Post Image";
                    postImage.classList.add('postImage');
                    imageContainer.appendChild(postImage);
                    postElement.appendChild(imageContainer);
                }
                
                // add text to postElement
                postElement.appendChild(postContent);

                // thumbs up icon
                const thumbsUpIcon = document.createElement('img');
                thumbsUpIcon.src = require('@/assets/thumb.png');
                thumbsUpIcon.alt = "Like Icon";
                thumbsUpIcon.classList.add('like-image');

                postElement.appendChild(thumbsUpIcon);
                const placeholder = this.$refs.dynamicContent;
                placeholder.appendChild(postElement);
                }
        }
  </script>
  <style scoped>
  .post-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.profile-image {
  width: 40px;
  height: 40px; 
  object-fit: cover;
  margin-bottom: 1em;
  margin-right: 1em;
}

div {
    min-width: 100px;
    display: block;
    visibility: visible;
    opacity: 1;
}

main > div > div { /*child selector*/
  background-color: rgb(224, 224, 224);
  border-radius: 10px;  
}

.post p { /*descendant selector?*/
  font-size: 1.5em;
  color: #212121;
  margin-bottom: 0em; 
}

.post{
  padding: 1em;
}

.post ~ .post { /*general sibling selector*/
  margin-top: 1em;
}

.profile-image + p {
  color: #434242; 
  font-size: 1em;
  margin-top: -0.25em;
}
.like-image{
  margin-bottom: -0.25em;
}

@media (max-width: 600px) {
  .postImage{
    width:100px;
    height: 100px;
    object-fit:cover;
  }
  .profile-image {
    width: 30px;
    height: 30px;
    object-fit: cover;
  }
  .post p {
    font-size: 0.9em;
  }
  .profile-image + p {
    color: #434242; 
    font-size: 0.7em;
  }
  
}
  </style>

