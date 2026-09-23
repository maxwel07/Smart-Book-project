 document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.slot').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.slot').forEach(s => s.classList.remove('selected'));
        btn.classList.add('selected');
      });
    });
  });

<<<<<<< HEAD

addReviewbtn = document.getElementById('write-review-btn')
form = document.getElementById('review-form')

addReviewbtn.addEventListener('click', () => {
  form.classList.toggle('open')
=======
const reviewButton = document.getElementById('write-review-btn');
const reviewForm = document.getElementById('review-form');

reviewButton.addEventListener('click', function click(){
  reviewForm.classList.toggle('open');
>>>>>>> 98bcece778846efd2d4b61364bb38fdb7dcdc270
})