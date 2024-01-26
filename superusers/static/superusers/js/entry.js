const ctx = document.getElementById('myChart');

new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
      label: '# of Votes',
      data: [12, 19, 3, 5, 2, 3],
      borderWidth: 1
    }]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});


//Add One More Box
class Form{

  //  AddButton = document.getElementById("AddMore");
    constructor(){

    }

    AddOneMoreBox(){
        let targetDiv = document.getElementById("insertInto");
        
        let HtmlToInsert =` <div class="row">

        <div class="col-sm-8" style="display: flex; flex-direction: row;">
         <!-- ........................... -->
        <div class="mx-4 mt-3"><label for="iType">Investment Type</label>
        
            <select name="iType" id="iType" class="form-control">
            <option value="individual">Individual</option>
            <option value="common">Common</option>
            
            
            </select></div>
        
        
        <div class="mx-4 mt-3">
            <label for="iCategory">Investment Category</label>
        
        <select name="iCategory" id="iCategory" class="form-control">
        <option value="Equity">Equity</option>
        <option value="Crypto">Crypto</option>
        <option value="Mutual Fund">Mutual Fund</option>
        <option value="F&O">F&O</option>
        <option value="Other">Other</option>
        
        
        </select>
        
        </div>
        
        <div class="mx-4 mt-3"><label for="iAmmount"><b>₹</b> Ammount</label>
            <input type="text" class="form-control" id="iAmmount">
            </div>
            
            <div class="mx-2 mt-4"><input title="Remove" type="button" class="btn btn-danger" value=" - " style="margin-top: 14px;"></div>
        </div> <hr class="mt-2">`;

        targetDiv.innerHTML += HtmlToInsert;

    }
}

form = new Form();
let button  = document.getElementById("AddMore");
button.onclick = () => {
    console.log("hello");
    form.AddOneMoreBox();
};