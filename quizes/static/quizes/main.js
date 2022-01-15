
//[...] converts the below to an array so that forEach can be used
const modalBtns=[...document.getElementsByClassName('modal-button')] //returns an HTML collection (multiple buttons)
const modalBody=document.getElementById('modal-body-confirm') //div inside the modal
const startBtn=document.getElementById('start-button') //'yes' inside the modal
const currentUrl=window.location.href
//for list of modal buttons
modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    //picking the value of the custom html attributes set in the main.html for each modal button
    const pk=modalBtn.getAttribute('data-pk')
    const name=modalBtn.getAttribute('data-quiz')
    const questions=modalBtn.getAttribute('data-questions')
    const difficulty=modalBtn.getAttribute('data-difficulty')
    const time=modalBtn.getAttribute('data-time')
    const passing_score=modalBtn.getAttribute('data-passing-score')

    //inject HTML code into the modal body using backticks
    modalBody.innerHTML=`
        <div class="h5 mb-3">Are you sure you want to begin "<b>${name}</b>"?</div>
        <div class="text muted">
            <ul>
                <li>Difficulty : <b>${difficulty}</b></li>
                <li>No. of questions : <b>${questions}</b></li>
                <li>Passing Score : <b>${passing_score}</b></li>
                <li>Time : <b>${time}</b></li>
            </ul>
        </div>
    `
    //for each 'Yes' button inside a modal
    startBtn.addEventListener('click', ()=>{
        window.location.href=currentUrl+pk
    })
}))

