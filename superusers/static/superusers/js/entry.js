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
class Form {
    Invidial = new Array();
    Common = new Array();
    body = new Object();
    total = 0;
    index = 0
    isRemoveButtonAvailable = false
    //  AddButton = document.getElementById("AddMore");
    constructor() {

    }

    AddOneMoreBox() {
        let targetDiv = document.getElementById("insertInto");
        var newDiv = document.createElement('div');
        this.index++;
        let HtmlToInsert = ` <div class="row rmv${this.index}" id="div${this.index}">

        <div class="col-sm-8" style="display: flex; flex-direction: row;">
         <!-- ........................... -->
        <div class="mx-4 mt-3"><label for="iType">Investment Type</label>
        
            <select name="iType" id="iType" class="form-control amm">
            <option value="individual">Individual</option>
            <option value="common">Common</option>
            
            
            </select></div>
        
        
        <div class="mx-4 mt-3">
            <label for="iCategory">Investment Category</label>
        
        <select name="iCategory" id="iCategory" class="form-control amm">
        <option value="Equity">Equity</option>
        <option value="Crypto">Crypto</option>
        <option value="Mutual Fund">Mutual Fund</option>
        <option value="F&O">F&O</option>
        <option value="Other">Other</option>
        
        
        </select>
        
        </div>
        
        <div class="mx-4 mt-3"><label for="iAmmount"><b>₹</b>Investment Ammount</label>
            <input type="number" class="form-control amt" id="iAmmount">
            </div>
            
            <div class="mx-2 mt-4"><input title="Remove" type="button" class="btn btn-danger rmv" id="rmv${this.index}" value=" - " style="margin-top: 14px;"></div>
        </div> <hr class="mt-2">`;
        newDiv.innerHTML = HtmlToInsert;
        targetDiv.appendChild(newDiv);
       // targetDiv.innerHTML += HtmlToInsert;
        this.isRemoveButtonAvailable = true;

    }

    RemoveInputBox(targetClassName) {
        if (this.isRemoveButtonAvailable) {
            document.getElementsByClassName(targetClassName)[0].remove();
        }
        if(document.getElementsByClassName("rmv").length==0) {this.isRemoveButtonAvailable = false;}
    }

    ManageAllInputBox(){
        this.Invidial = []
        this.Common = []
        this.total = 0
        Array.from(document.forms[0].elements).forEach((e,i)=>{
            if(e.id == 'iAmmount')
                if(e.value.trim().length != 0)
                    this.total += parseFloat(e.value) 
            if(e.id == "iType")
                if(e.value == "individual")
                  if(Array.from(e.classList).includes("amm"))
                    this.Invidial.push(document.getElementsByClassName("amt")[i].value)
        });
     console.log(this.total,this.Invidial);
    }
}

form = new Form();
//adding the form
let button = document.getElementById("AddMore");
button.onclick = () => {
    form.AddOneMoreBox();
    //for removing the form
    if (form.isRemoveButtonAvailable) {
        let removeButton = document.getElementsByClassName("rmv");

        Array.from(removeButton).forEach(e => {
            e.addEventListener("click", (targetButton) => {
                form.RemoveInputBox(e.id);
            })
        });
    }
};

//for submitting the button
let submitButton = document.getElementById("Submit");
submitButton.addEventListener("click", (targetButton) => {
    form.ManageAllInputBox();
});
