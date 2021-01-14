Vue.component('algorithms', {
  data: function () {
    return {
      pkg: "",
    }
  },
  methods: {
    get: function (val) {
      this.pkg = val;
      axios.get(`http://127.0.0.1:5000/api/${this.pkg}`)
        .then((response) => {
          if (response.data.error == "error") {
            console.log("bakend error");
          } else {
            console.log(response.data.result);
          }
        }, (err) => {
          console.log("frontend error", err);
        })
    },
    post: function (val) {
      this.pkg = val;
      axios.post(`http://127.0.0.1:5000/api/${this.pkg}`, {
        "params": JSON.stringify(this.pkg)
      })
        .then((response) => {
          if (response.data.error == "error") {
            console.log("bakend error");
          } else {
            console.log(response.data.result);
          }
        }, function (err) {
          console.log("frontend error", err);
        })
    },
  },
  template:
    `
<div>
<el-button type="primary" round @click="get(1)">get</el-button>
<el-button type="primary" round @click="post(2)">post</el-button>
</div>
`
})