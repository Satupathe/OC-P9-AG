/*var radios = document.getElementsByName('ratingValue');
console.log(radios);

for(const element of radios){
    if (element.checked){
        console.log(element.value)
    }
}*/



window.onload = () => {
    var values = document.getElementsByName("ratingValue");
    console.log(values);
    var result = document.getElementsByName("ratingResult")[0];
    console.log(result.value);
     

    for(var value of values){
        
        value.addEventListener("click", function(){
            console.log(this.value)
            result.value = this.value;
            console.log(result.value)

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
}