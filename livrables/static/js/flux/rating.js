window.onload = () => {
    const stars = document.querySelectorAll(".la-star");
    const rating = document.querySelector("#rating");
     

    for(star of stars){
        // On écoute le survol
        star.addEventListener("mouseover", function(){
            resetStars();
            this.style.color = "red";
            this.classList.add("las");
            this.classList.remove("lar");
            let previousStar = this.previousElementSibling;

            while(previousStar){
                previousStar.style.color = "red";
                previousStar.classList.add("las");
                previousStar.classList.remove("lar");
                previousStar = previousStar.previousElementSibling;
            }
        });

        star.addEventListener("click", function(){
            rating.value = this.dataset.value;
        });

        star.addEventListener("mouseout", function(){
            resetStars(rating.value);
        });
    }

    /**
     * @param {number} rating 
     */
    function resetStars(rating = 0){
        for(star of stars){
            if(star.dataset.value > rating){
                star.style.color = "black";
                star.classList.add("lar");
                star.classList.remove("las");
            }else{
                star.style.color = "red";
                star.classList.add("las");
                star.classList.remove("lar");
            }
        }
    }
    var rateValue = document.getElementsByClassName("displayRate").item(0).innerHTML;
    var dataRatings = document.getElementsByClassName("show-star");
    console.log(rateValue);
    console.log(dataRatings);

    function star(rateValue) {   
        for (datarating in dataRatings){
            console.log(datarating);
            if(datarating.value <= rateValue){
                datarating.style.backgroundColor = "red"
            };
        };
    }
    star()
}