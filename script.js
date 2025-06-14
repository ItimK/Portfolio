function copyPhoneNumber(event) {
  event.preventDefault(); // Prevent default link behavior
  const phoneNumber = "+1 (912) 272-2019";
  navigator.clipboard.writeText(phoneNumber).then(() => {
    alert("Phone number copied to clipboard!");
  }).catch(err => {
    console.error("Failed to copy!", err);
  });
}

const scriptURL = 'https://script.google.com/macros/s/AKfycbzlOPp4TP8VyNhG8JOegsMgSXaFH0Mbe_TXaaCHSgoMSofsENKjXIYBv5tMA-c_7r1R/exec'

const form = document.forms['contact-form']

form.addEventListener('submit', e => {
  
  e.preventDefault()
  
  fetch(scriptURL, { method: 'POST', body: new FormData(form)})
  .then(response => alert("Message sent successfully, thank you!" ))
  .then(() => { window.location.reload(); })
  .catch(error => console.error('Error!', error.message))
})



