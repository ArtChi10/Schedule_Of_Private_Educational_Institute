'use strict';

(function toggleAsideCollapse() {
  const aside = document.querySelector('.aside'),
    control = aside.querySelector('.aside__switch');

  const CLASSES = {
    asideExpanded: 'aside--expanded',
    controlToClose: 'aside__switch--close'
  }

  const onControlClick = (e) => {
    e.preventDefault();
    aside.classList.toggle(CLASSES.asideExpanded);
    control.classList.toggle(CLASSES.controlToClose);
  }

  control.addEventListener('click', onControlClick);
})();