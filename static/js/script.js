const faders = document.querySelectorAll('.fade-in')

// Function to animate item on scroll
// Help from https://www.youtube.com/watch?v=huVJW23JHKQ&t=318s
const appearOptions = {
    threshold: 1,
};

const appearOnScroll = new IntersectionObserver(function(
    entries, appearOnScroll
) {
    entries.forEach(entry => {
        if (!entry.isIntersecting) {
            return;
        } else {
            entry.target.classList.add("appear");
            appearOnScroll.unobserve(entry.target);
        }
    });
    
},appearOptions)

faders.forEach(fader => {
    appearOnScroll.observe(fader)
})

// Function to remove messages 
setTimeout(function() {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 4000);
