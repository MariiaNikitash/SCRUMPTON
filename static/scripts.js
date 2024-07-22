// JavaScript to toggle the signup and signin sections visibility

document.getElementById('signup-tab-link').addEventListener('click', function(e) {
    e.preventDefault();
    toggleVisibility('signup');
});

document.getElementById('signin-tab-link').addEventListener('click', function(e) {
    e.preventDefault();
    toggleVisibility('signin');
});

document.getElementById('close-signup').addEventListener('click', function() {
    document.getElementById('signup').style.display = 'none';
});

document.getElementById('close-signin').addEventListener('click', function() {
    document.getElementById('signin').style.display = 'none';
});

function toggleVisibility(sectionId) {
    const signupSection = document.getElementById('signup');
    const signinSection = document.getElementById('signin');
    if (sectionId === 'signup') {
        signupSection.style.display = signupSection.style.display === 'block' ? 'none' : 'block';
        signinSection.style.display = 'none';
        if (signupSection.style.display === 'block') {
            signupSection.scrollIntoView({behavior: "smooth"});
        }
    } else if (sectionId === 'signin') {
        signinSection.style.display = signinSection.style.display === 'block' ? 'none' : 'block';
        signupSection.style.display = 'none';
        if (signinSection.style.display === 'block') {
            signinSection.scrollIntoView({behavior: "smooth"});
        }
    }
}

// Ensure sections are hidden initially
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('signup').style.display = 'none';
    document.getElementById('signin').style.display = 'none';
   
});
