/**
 * @param {number[]} ranks
 * @param {number} cars
 * @return {number}
 */
var validate = function(ranks, cars, max_time){
    let num_cars = cars
    for(rank of ranks){
        num_cars -= Math.floor(Math.sqrt(max_time / rank))
    }
    return num_cars <= 0
}

var repairCars = function(ranks, cars) {
    let shortest = 0
    let longest = -1
    for(rank of ranks){
        if(rank > longest){
            longest = rank
        }
    }

    longest = longest * cars * cars
    while(shortest < longest){
        let mid = Math.floor((shortest + longest) / 2)
        if(validate(ranks, cars, mid)){
            longest = mid
        }else{
            shortest = mid + 1
        }
    }

    return shortest
};