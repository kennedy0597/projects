function fileRead(path)
{
    let retarr =[];
    var fs = require('fs');
    return fs.readFileSync(path).toString();
}

module.exports.fileRead=fileRead;

function fileToArray(path)
{
    let retarr = [];
    var fs =require('fs');
    var array = fs.readFileSync(path).toString().split("\n");
    for(let i = 0; i<array.length;i+=1){
        //console.log(array[i]);
        if(array[i].length>0)
        retarr.push(array[i]);

    }
return retarr;


}
module.exports.fileToArray= fileToArray;