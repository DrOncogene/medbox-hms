let currSlide = 0;

const heroSlides = document.querySelectorAll('.hero-slide');
const NUMSLIDES = heroSlides.length - 1;

heroSlides.forEach((slide, idx) => {
  slide.style.transform = `translateX(${idx * 100}%)`;
});

function heroScroll() {
  if (currSlide === NUMSLIDES) { currSlide = 0 }
  else currSlide += 1;

  const heroSlides = document.querySelectorAll('.hero-slide');
  const indicators = document.querySelectorAll('.indicator');
  heroSlides.forEach((slide, idx) => {
    slide.style.transform = `translateX(${(idx - currSlide) * 100}%)`;
    indicators?.forEach((ind, indIdx) => {
      if (ind.classList.contains('active')) {
        ind.classList.remove('active');
      }
      if (indIdx === currSlide) {
        ind.classList.add('active');
      }
    });
  });
}

setInterval(heroScroll, 4000);

// function isVisible (el) {
//   let rect = el.getBoundingClientRect();

//   return (
//       rect.left >= 0 &&
//       rect.right < (window.innerWidth || document.documentElement.clientWidth)
//   );
// }

// function scrollCards(e, cards, forwards) {
//   e.preventDefault();
//   if (forwards && isVisible(cards[cards.length - 1])) return;
//   if (!forwards && isVisible(cards[0])) return;

//   cards.forEach((card) => {
//     const translate = card.style.transform
//     const currPos = Number(translate.substring(11, translate.indexOf('%')));
//     if (forwards)
//       card.style.transform = `translateX(${currPos - 100}%)`;
//     else
//       card.style.transform = `translateX(${currPos + 100}%)`;
//   });
// }

// const prevBtns = document.querySelectorAll('.prev-btn');
// const nextBtns = document.querySelectorAll('.next-btn');

// prevBtns.forEach((btn) => {
//   const sectionId = btn.parentElement.id;
//   const cards = document.querySelectorAll(`#${sectionId} .card`);

//   btn.addEventListener('click', (e) => scrollCards(e, cards, false));
// });

// nextBtns.forEach((btn) => {
//   const sectionId = btn.parentElement.id;
//   const cards = document.querySelectorAll(`#${sectionId} .card`);

//   btn.addEventListener('click', (e) => scrollCards(e, cards, true));
// });

// const cards = document.querySelectorAll(`#services .card`);
// let forwards = true;
// setInterval(() => {
//   if (isVisible(cards[cards.length - 1])) forwards = false;
//   if (isVisible(cards[0])) forwards = true;

//   scrollCards(new MouseEvent('click'), cards, forwards);
// }, 4000);
