var app = new Vue({
    el: '#app',
    data() {
        return {
            homeShow: true,
            algShow: false,
            toolShow: false
        }
    },
    mounted() {
        setInterval(() => {
            this.checkVisibility();
        }, 1000);
    },
    methods: {
        changeShow(key, keyPath) {
            if (key == "home") {
                this.homeShow = true;
                this.algShow = false;
                this.toolShow = false;
            }
            if (key == "tool") {
                this.homeShow = false;
                this.algShow = false;
                this.toolShow = true;
            }
            if (key[0] == "2") {
                this.homeShow = false;
                this.algShow = true;
                this.toolShow = false;
            }
        },
        checkVisibility: function () {
            let vs = document.visibilityState;
            let date = new Date(Date.now());
            if (vs == "visible") {
                document.title = "FinTech Algs - " + date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();
            }
        }
    }
});