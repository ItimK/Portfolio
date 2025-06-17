function copyPhoneNumber(event) {
  event.preventDefault(); // Prevent default link behavior
  const phoneNumber = "+1 (912) 272-2019";
  navigator.clipboard.writeText(phoneNumber).then(() => {
    alert("Phone number copied to clipboard!");
  }).catch(err => {
    console.error("Failed to copy!", err);
  });
}

// ===== Form 1 =====
const scriptURL1 = 'https://script.google.com/macros/s/AKfycbzlOPp4TP8VyNhG8JOegsMgSXaFH0Mbe_TXaaCHSgoMSofsENKjXIYBv5tMA-c_7r1R/exec';
const form1 = document.getElementById('contact-form');

if (form1) {
  form1.addEventListener('submit', e => {
    e.preventDefault();

    fetch(scriptURL1, { method: 'POST', body: new FormData(form1) })
      .then(response => {
        alert("Message sent successfully, thank you!");
        form1.reset();
      })
      .catch(error => {
        console.error('Error!', error.message);
        alert("Failed to send message.");
      });
  });
}

// ===== Form 2 =====
const scriptURL2 = 'https://script.google.com/macros/s/AKfycbwuqYpqd0arHNhoGyGINaxnuB90-3-8krHT-W_DBVzN48E1VAAGh_oW3KTm-TbrPjAM/exec';
const form2 = document.getElementById('marble-temple-feedback');

if (form2) {
  form2.addEventListener('submit', e => {
    e.preventDefault();

    fetch(scriptURL2, { method: 'POST', body: new FormData(form2) })
      .then(response => {
        alert("Message sent successfully, thank you!");
        form2.reset();
      })
      .catch(error => {
        console.error('Error!', error.message);
        alert("Failed to send message.");
      });
  });
}

// ===== Form 3 =====
const scriptURL3 = 'https://script.google.com/macros/s/AKfycbzFE4jelWqBhYqImmqHT2v27BlyfWNhHgrm1ys9cVezGdbzfU43vCsFlSn-UfD50QR_/exec';
const form3 = document.getElementById('chocolate-shop-feedback');

if (form3) {
  form3.addEventListener('submit', e => {
    e.preventDefault();

    fetch(scriptURL3, { method: 'POST', body: new FormData(form3) })
      .then(response => {
        alert("Message sent successfully, thank you!");
        form3.reset();
      })
      .catch(error => {
        console.error('Error!', error.message);
        alert("Failed to send message.");
      });
  });
}

// ===== Form 4 =====
const scriptURL4 = 'https://script.google.com/macros/s/AKfycbziPNhc3-wzhXe4yHNvI1Y6taJ9gj5d82jgzv9JAq-ncpRVEGB530MYSgkqPRTWRkXF/exec';
const form4 = document.getElementById('waterdrop-feedback');

if (form4) {
  form4.addEventListener('submit', e => {
    e.preventDefault();

    fetch(scriptURL4, { method: 'POST', body: new FormData(form4) })
      .then(response => {
        alert("Message sent successfully, thank you!");
        form4.reset();
      })
      .catch(error => {
        console.error('Error!', error.message);
        alert("Failed to send message.");
      });
  });
}

// ===== Form 5 =====
const scriptURL5 = 'https://script.google.com/macros/s/AKfycbwYqzYW1kQO446zkDSiOp9Um3Yx9ikLPx_Sx98ZUyKwBSyVsJkjA5938h1KBrsKSMr-KQ/exec';
const form5 = document.getElementById('silent-helper-feedback');

if (form5) {
  form5.addEventListener('submit', e => {
    e.preventDefault();

    fetch(scriptURL5, { method: 'POST', body: new FormData(form5) })
      .then(response => {
        alert("Message sent successfully, thank you!");
        form5.reset();
      })
      .catch(error => {
        console.error('Error!', error.message);
        alert("Failed to send message.");
      });
  });
}

// ===== Form 6 =====
const scriptURL6 = 'https://script.google.com/macros/s/AKfycbx7iBSu20Bwhh__VCvT78MkzK_sU3QZlqkK9-CKIrZnfrJ34Bk4yS3mb7FOp_4iT0eu/exec';
const form6 = document.getElementById('woodland-grave-feedback');

if (form6) {
  form6.addEventListener('submit', e => {
    e.preventDefault();

    fetch(scriptURL6, { method: 'POST', body: new FormData(form6) })
      .then(response => {
        alert("Message sent successfully, thank you!");
        form6.reset();
      })
      .catch(error => {
        console.error('Error!', error.message);
        alert("Failed to send message.");
      });
  });
}


// --------------------- SIDE MENU ---------------------

var sidemenu = document.getElementById("nav-bar");

function openmenu(){
  sidemenu.style.right = "0";
}
function closemenu(){
  sidemenu.style.right = "-400px";
}





