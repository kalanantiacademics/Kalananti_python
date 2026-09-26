import re

with open('level1/main_deck.js', 'r') as f:
    js = f.read()

# Modify renderSlide
render_slide_new = """function renderSlide(){
  const slides=deckData[currentMeeting], slide=slides[currentIndex];
  dom.meetingPill.textContent=`Meeting ${currentMeeting}`; dom.sectionPill.textContent=slide.sectionLabel;
  dom.objectivePill.hidden=!slide.objectiveId; dom.objectivePill.textContent=slide.objectiveId||'';
  dom.title.textContent=slide.title; dom.subtitle.textContent=slide.subtitle; dom.content.innerHTML=slide.content;
  dom.counter.textContent=`Slide ${currentIndex+1} / ${slides.length}`;
  const percent=((currentIndex+1)/slides.length)*100; dom.bar.style.width=`${percent}%`;
  dom.progress.setAttribute('aria-valuemax',String(slides.length)); dom.progress.setAttribute('aria-valuenow',String(currentIndex+1));
  dom.prev.disabled=currentIndex===0; dom.next.disabled=currentIndex===slides.length-1;
  dom.sectionSelector.value=slide.sectionId; dom.card.scrollTop=0; initSlideInteractions(); updateHash();
  
  // Trigger slide-in animation
  const stage = document.querySelector('.slide-stage');
  stage.classList.remove('animate-in');
  void stage.offsetWidth; // trigger reflow
  stage.classList.add('animate-in');
}"""

js = re.sub(r'function renderSlide\(\)\{.*?(?=\nfunction go\()', render_slide_new + '\n\n', js, flags=re.DOTALL)

with open('level1/main_deck.js', 'w') as f:
    f.write(js)
