document.addEventListener('DOMContentLoaded', function() {
  var phoneNumberInput = document.getElementById('phone-number');
  if (phoneNumberInput) {
    phoneNumberInput.addEventListener('focus', autofillPhoneNumber);
  }
});

function autofillPhoneNumber() {
  console.log('autofillPhoneNumber function called');
  var phoneNumberInput = document.getElementById('phone-number');
  if (phoneNumberInput.value === '') {
    phoneNumberInput.value = '+380';
  }
}