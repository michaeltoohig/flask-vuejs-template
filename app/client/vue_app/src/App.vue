<template>
  <div id="app">

    <b-navbar toggleable="md" type="dark" variant="secondary">
      <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
      <b-navbar-brand to="/">Home</b-navbar-brand>
      <b-collapse is-nav id="nav_collapse">
        <b-navbar-nav>
          <b-nav-item to="/api">API Sample</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <div id="logos">
      <p>
        <img src="./assets/vue-logo.png">
        <span id="plus">+</span>
        <img src="./assets/flask-logo.png">
      </p>
    </div>

    <router-view/>

    <!-- FORK Me -->
    <a href="https://github.com/michaeltoohig/flask-vuejs-template"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_right_orange_ff7600.png" alt="Fork me on GitHub"></a>

  </div>
</template>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
#plus {
  padding: 0 20px 0 20px;
  display: inline-block;
  font-size: 50px;
  vertical-align: top;
  line-height: 100px;
}

</style>
