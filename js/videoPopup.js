(function () {
    const videoLink = document.getElementById('videoLink');
    const videoPopup = document.getElementById('videoPopup');
    const closePopup = document.getElementById('closePopup');
    const youtubeVideo = document.getElementById('youtubeVideo');

    videoLink.addEventListener('click', (e) => {
        e.preventDefault();
        youtubeVideo.src = 'https://www.youtube.com/embed/' + videoLink.getAttribute('video-id');
        videoPopup.classList.remove('hidden');
    });

    closePopup.addEventListener('click', () => {
        youtubeVideo.src = '';
        videoPopup.classList.add('hidden');
    });

    videoPopup.addEventListener('click', (e) => {
        if (e.target === videoPopup) {
        youtubeVideo.src = '';
        videoPopup.classList.add('hidden');
        }
    })
})();