var tickets = document.getElementsByClassName("ticket")
console.log(tickets)



function star(tickets) {   
    for(const ticket of tickets){
        var rateValue = ticket.getElementsByClassName("displayRate").item(0).innerText;
        console.log(rateValue)
        if (rateValue != ""){

            var dataRatings = ticket.getElementsByClassName("show-star");
            
            console.log(dataRatings)
    
            for (const datarating of dataRatings){
                if(datarating.getAttribute('value') <= rateValue){
                    datarating.getElementsByTagName('img')[0].style.backgroundColor = 'red';
                };
            };
        }
    }
}
star(tickets)
    
