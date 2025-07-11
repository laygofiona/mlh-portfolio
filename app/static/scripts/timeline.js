

document.getElementById('timeline-form').addEventListener('submit', async function(event) {
    event.preventDefault(); 

    // Collect form data
    const form = document.getElementById('timeline-form');
    const formData = new FormData(form);

    try {
        const response = await fetch('/api/timeline_post', {
            method: 'POST',
            body: formData
        });

        if(response.ok){
            console.log('Success:', response); 
            alert('Post submitted successfully!');
            // reload the page
            window.location.reload(true);
        } else {
            alert('An error occurred while submitting the form.');
        }
    } catch (error) {
        console.error('Error:', error);
    }
})

document.addEventListener('DOMContentLoaded', function () {
    fetch('/api/timeline_post')
        .then(response => {
            if (!response.ok) throw new Error('Network response was not OK');
            return response.json();
        })
        .then(data => {
            console.log('Posts:', data);
            displayPosts(data.timeline_posts); 
        })
        .catch(error => {
            console.error('Error fetching posts:', error);
        });
});


function displayPosts(posts) {
    const container = document.getElementById('posts-container');
    container.innerHTML = ''; // Clear if reloading

    if(posts.length < 1){
        const textNone = document.createElement('p');
        textNone.innerText = 'No posts at this time. Create a post.'
        textNone.classList.add('none')
        container.appendChild(textNone)
    } else {
        posts.forEach(post => {
        const postDiv = document.createElement('div');
        postDiv.classList.add('post');
        postDiv.innerHTML = `
            <h4>${post.name} (${post.email})</h4>
            <p>${post.content}</p>
            ${post.created_at ? `<small>${new Date(post.created_at).toLocaleString()}</small>` : ''}
        `;
        container.appendChild(postDiv);
        });
    }

    
}
