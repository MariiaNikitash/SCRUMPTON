// Get references to radio buttons and image containers
const radios = document.querySelectorAll('input[name="radio"]');
const imageContainers = document.querySelectorAll('.image-container');

// Function to toggle image visibility
function toggleImage(imageId) {
    imageContainers.forEach(container => {
        container.style.display = container.id === imageId ? 'block' : 'none';
    });
}

// Initially show small room image
toggleImage('image-small');

// Add event listeners to radio buttons
radios.forEach(radio => {
    radio.addEventListener('click', function() {
        toggleImage(`image-${this.value}`);
    });
});

