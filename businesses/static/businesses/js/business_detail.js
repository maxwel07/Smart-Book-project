 document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.slot').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.slot').forEach(s => s.classList.remove('selected'));
        btn.classList.add('selected');
      });
    });
  });


addReviewbtn = document.getElementById('write-review-btn')
form = document.getElementById('review-form')

addReviewbtn.addEventListener('click', () => {
  form.classList.toggle('open')
})