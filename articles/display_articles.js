let pageNum = 1;

function changePage(delta)
{
    pageNum += delta;
    if (pageNum < 1)
    {
        pageNum = 1;
    }
    if (pageNum == 1)
    {
        document.getElementById("PrevButton").style.display = "none";
    }
    else
    {
        document.getElementById("PrevButton").style.display = "block";
    }
}