 document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.slot').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.slot').forEach(s => s.classList.remove('selected'));
        btn.classList.add('selected');
      });
    });
  });

const reviewButton = document.getElementById('write-review-btn');
const reviewForm = document.getElementById('review-form');

reviewButton.addEventListener('click', function click(){
  reviewForm.classList.toggle('open');
})