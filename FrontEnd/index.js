var app = new Vue({
    el: '#app',
    data() {
        return {
            problemNo: "",
            codes:'',
            menuShow: true,
            width: { width: (parseInt(window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth)) + 'px' },
            height: { height: (parseInt(window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight) - 128) + 'px' }
        }
    },
    mounted() {
        setInterval(() => {
            this.checkVisibility();
        }, 1000)
    },
    methods: {
        changeMenuShow: function () {
            this.menuShow = !this.menuShow;
        },
        checkVisibility: function () {
            let vs = document.visibilityState;
            let date = new Date(Date.now());
            if (vs == "visible") {
                document.title = "Algorithms - " + date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();
            }
        },
        changeLine:function(e){
            if(e.key==="Tab"){
                e.preventDefault();
                if(this.codes[this.codes.length-1]!=" "){
                    this.codes = this.codes+"\n    "
                }else{
                    this.codes = this.codes+"    "
                }
                
            }
        },
        changeProblem: function () {
            this.problemNo = this.problemNo || 1;
            axios.get(`http://127.0.0.1:5000/api/${this.problemNo}`)
                .then((response) => {
                    if (response.data.error == "error") {
                        let left = document.getElementById("left");
                        left.innerHTML = "Client Error";
                        this.codes = "Client Error";
                    } else {
                        let left = document.getElementById("left");
                        left.innerHTML = response.data.left;
                        this.codes = "";
                    }
                }, (err) => {
                    let left = document.getElementById("left");
                    left.innerHTML = "Server Error";
                    this.codes = "Server Error";
                })
        },
        testResult: function () {
            axios.post(`http://127.0.0.1:5000/api/${this.problemNo}`, {
                "name": JSON.stringify(this.problemNo)
            })
                .then((response) => {
                    if (response.data.error == "error") {
                        let left = document.getElementById("left");
                        left.innerHTML = "Client Error";
                        this.codes = "Client Error";
                    } else {
                        let result = response.data.result;
                        this.codes = `Correct Result is: ${result}\n` + this.codes;
                    }
                }, function (err) {
                    let left = document.getElementById("left");
                    left.innerHTML = "Server Error";
                    this.codes = "Server Error";
                })
        },
    }
});