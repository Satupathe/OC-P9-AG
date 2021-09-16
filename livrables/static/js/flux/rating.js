var tickets = document.getElementsByClassName("ticket")

function star(tickets) {   
    for(const ticket of tickets){
        var rateValue = ticket.getElementsByClassName("displayRate").item(0);
        console.log(rateValue)
        if (rateValue === null){
            continue
        } else {
            if (rateValue != ""){
                var dataRatings = ticket.getElementsByClassName("show-star");
                for (const datarating of dataRatings){
                    if(datarating.getAttribute('value') <= rateValue.innerHTML){
                        datarating.getElementsByTagName('img')[0].style.backgroundColor = 'red';
                    };
                };
            }
        }
    }
}
star(tickets)
    
