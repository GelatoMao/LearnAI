<template>
  <div class="home">
    用户名<input type="text" v-model="username" />
    <br />
    密码<input type="password" v-model="password" />
    <br />
    <button @click="login">登录</button>

    <div class="box">
      <div v-for="item in lists" :key="item.id">
        <p @click="login">用户名:{{ item.username }}</p>
        <p>密码：{{ item.password }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import api from "../utils/api.js"
export default {
  name: "Home",
  data() {
    return {
      username: "",
      password: "",
      lists: [],
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password
      // 请求后台登录接口
      let url = api.api + "/user/list"
      this.axios.get(url).then((res) => {
        console.log(res)
        this.lists = res.data
      })
    },
  },
}
</script>

<style></style>
