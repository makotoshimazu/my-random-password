function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

class RandomGenerator {
  constructor(length, options) {
    this._length = length;
    if (!'numbers' in options ||
        !'lower_alphabets' in options ||
        !'upper_alphabets' in options ||
        !'symbols' in options ||
        !'symbols_to_use' in options) {
      console.error(`lack of params: ${options}`);
      return;
    }
    let candidates = '';
    if (options['numbers'])
      candidates += '0123456789';
    if (options['lower_alphabets'])
      candidates += 'abcdefghijklmnopqrstuvwxyz';
    if (options['upper_alphabets'])
      candidates += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    if (options['symbols'])
      candidates += options['symbols_to_use'];
    this._candidates = candidates;
  }

  generate() {
    if (this._candidates.length === 0) {
      toastr.warning('No "Type" has been specified.');
      console.error('No type has been specified')
      return '';
    }
    let out = '';
    for (let i = 0; i < this._length; i++) {
      let index = getRandomInt(0, this._candidates.length - 1);
      out += this._candidates[index];
    }
    return out;
  }
}

// Select and copy the contents of |event.target|.
// |event|: MouseEvent.
function copyInnerText(event) {
  document.getSelection().selectAllChildren(event.target);
  let result = document.execCommand('copy');
  if (!result) {
    toastr.warning('Copy failed.');
    console.error(`Copy failed: ${result}`);
    return;
  }
  toastr.success('Copied to your clipboard.');
  console.log(`Copied: ${event.target.innerText}`);
}

document.getElementById('btn-generate').addEventListener('click', () => {
  let params = document.getElementById('form-params');
  let length = parseInt(params.length.value, 10);
  let numbers = params.numbers.checked;
  let lower_alphabets = params.lower_alphabets.checked;
  let upper_alphabets = params.upper_alphabets.checked;
  let symbols = params.symbols.checked;
  let symbols_to_use = document.getElementById('symbols-to-use').value;
  let generator = new RandomGenerator(length, {
    numbers: numbers,
    lower_alphabets: lower_alphabets,
    upper_alphabets: upper_alphabets,
    symbols: symbols,
    symbols_to_use: symbols_to_use
  });

  let out = generator.generate();
  let out_span = document.createElement('span');
  out_span.classList.add('password');
  out_span.innerText = out;
  out_span.addEventListener('click', copyInnerText);

  let out_div = document.createElement('div');
  out_div.appendChild(out_span);
  let passwords = document.querySelector('.passwords');
  passwords.appendChild(out_div);
});

if ('serviceWorker' in navigator &&
    !navigator.serviceWorker.controller) {
  navigator.serviceWorker.register('sw.js');
}

addEventListener('load', () => {
  console.log('loaded.');
  toastr.options = {
    "closeButton": true,
    "debug": true,
    "newestOnTop": true,
    "progressBar": false,
    "positionClass": "toast-bottom-right",
    "preventDuplicates": false,
    "onclick": null,
    "showDuration": "200",
    "hideDuration": "200",
    "timeOut": "3000",
    "extendedTimeOut": "1000",
    "showEasing": "swing",
    "hideEasing": "swing",
    "showMethod": "fadeIn",
    "hideMethod": "fadeOut"
  }
});
