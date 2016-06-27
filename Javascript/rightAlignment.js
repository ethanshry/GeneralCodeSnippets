//Right Align Item with Right most item in a list of items
function positionFilters() {
    var rightmostElement = 0;
    //loop through each dashcard
    $(".dashcard-wrapper").each(function (index) {
        ($(this).position().left + $(this).width()) >= rightmostElement ? rightmostElement = ($(this).position().left + $(this).width()) : rightmostElement = rightmostElement
    });
    //accounts for offset of element due to element width
    $('#filter-list').css('left', rightmostElement - $('#filter-list').width());
}

$(document).ready(positionFilters);
$(window).resize(positionFilters);