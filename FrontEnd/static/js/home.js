Vue.component('home', {
  data: function () {
    return {
      userLocation: "",
      notificationShow:true,
      reverse: true,
        activities: [{
          content: 'Lecture 1',
          timestamp: '2021-01-23',
          size: 'large',
          color: '#0bbd87'
        }, {
          content: 'Lecture 2',
          timestamp: '2021-01-30',
          size: 'large',
          color: '#0bbd87'
        }, {
          content: 'Lecture 3',
          timestamp: '2021-02-06',
          size: 'large',
          color: '#0bbd87'
        }, {
          content: 'Lecture 4',
          timestamp: '2021-02-13',
          size: 'large',
          color: '#0bbd87'
        }, {
          content: 'Lecture 5',
          timestamp: '2021-02-20',
          size: 'large',
          color: '#0bbd87'
        }, {
          content: 'Lecture 6',
          timestamp: '2021-02-27',
          size: 'large',
          color: '#0bbd87'
        }, {
          content: 'Lecture 7',
          timestamp: '2021-03-06',
          size: 'large',
          color: '#0bbd87'
        }, {
          content: 'Lecture 8',
          timestamp: '2021-03-13',
          size: 'large',
          color: '#0bbd87'
        }, {
          content: 'Lecture 9',
          timestamp: '2021-03-20',
          size: 'large',
          color: '#0bbd87'
        }, {
          content: 'Lecture 10',
          timestamp: '2021-03-27',
          size: 'large',
          color: '#0bbd87'
        }, {
          content: 'Lecture 11',
          timestamp: '2021-04-03',
          size: 'large',
          color: '#0bbd87'
        }, {
          content: 'Lecture 12',
          timestamp: '2021-04-10',
          size: 'large',
          color: '#0bbd87'
        }, {
          content: 'Lecture 13',
          timestamp: '2021-04-17',
          size: 'large',
          color: '#0bbd87'
        }, {
          content: 'Lecture 14',
          timestamp: '2021-04-24',
          size: 'large',
          color: '#0bbd87'
        }, {
          content: 'Lecture 15',
          timestamp: '2021-04-30',
          size: 'large',
          color: '#0bbd87'
        }
      ]
    }
  },
  mounted() {
    this.getLocation();
  },
  methods: {
    sendNotification(position) {
      let latitude =
        position.coords.latitude > 0
          ? position.coords.latitude + " N"
          : position.coords.latitude + " S";
      let longitude =
        position.coords.longitude > 0
          ? position.coords.longitude + " E"
          : position.coords.longitude + " W";
      this.userLocation = `Location Safety Notification: You are now at (${latitude}, ${longitude}), have access to Algorithms.`;
      var n = new Notification("Location: ", {
        body: this.userLocation,
        tag: "eggroup",
        requireInteraction: false,
        data: {
          loc: this.userLocation,
        },
      });
      n.onclick = function () {
        n.close();
      };
    },
    getLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(this.sendNotification);
      }
    },
    changeNotification(){
      this.notificationShow = false;
    }
  },
  template:
`
<div>
<!-- 位置提醒框 -->
<h3 class="notify" @click="changeNotification" v-show="notificationShow">
<i class="el-icon-caret-top"></i>
{{userLocation}}
</h3>

<!-- 排序选择 -->
<div class="radio center">
  <el-radio-group v-model="reverse">
    <el-radio :label="true">Descending</el-radio>
    <el-radio :label="false">Ascending</el-radio>
  </el-radio-group>
</div>

<!-- 时间轴 -->
<el-timeline :reverse="reverse">
  <el-timeline-item
    v-for="(activity, index) in activities"
    :key="index"
    :timestamp="activity.timestamp"
    :color="activity.color"
    :size="activity.size"
    >
      <el-card>
        {{activity.content}}
      </el-card>
  </el-timeline-item>
</el-timeline>

</div>
`
})