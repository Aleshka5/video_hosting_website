<template>
  <nav class="navbar navbar-expand navbar-light bg-white static-top osahan-nav sticky-top">
    &nbsp;&nbsp;
    <button class="btn btn-link btn-sm text-secondary order-1 order-sm-0" id="sidebarToggle">
      <i class="fas fa-bars"></i>
    </button> &nbsp;&nbsp;
    <a class="navbar-brand mr-1" href="/"><img class="img-fluid" alt="" src="@/assets/img/logo.png"></a>
    <!-- Navbar Search -->
    <form
      class="d-none d-md-inline-block form-inline ml-auto mr-0 mr-md-5 my-2 my-md-0 osahan-navbar-search">
      <div class="input-group">
        <input type="text" class="form-control" placeholder="Поиск...">
        <div class="input-group-append">
          <button class="btn btn-light" type="button">
            <i class="fas fa-search"></i>
          </button>
        </div>
      </div>
    </form>
    <!-- Navbar -->
    <ul class="navbar-nav ml-auto ml-md-0 osahan-right-navbar">
      <li class="nav-item mx-1">
        <a class="nav-link" href="/upload">
          <i class="fas fa-plus-circle fa-fw"></i>
          Загрузить видео
        </a>
      </li>

      <li class="nav-item dropdown no-arrow osahan-right-navbar-user">
        <a class="nav-link dropdown-toggle user-dropdown-link" href="#" id="userDropdown"
           role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <img alt="Avatar" src="@/assets/img/user.png">
          {{ userName }}
        </a>

      </li>

      <li class="nav-item osahan-right-navbar-user">
        <a class="nav-link" href="#" v-on:click="logout">
          <i class="fas fa-arrow-circle-right fa-fw"></i>
        </a>
      </li>
    </ul>
  </nav>
  <div id="wrapper">
    <!-- Sidebar -->
    <ul class="sidebar navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="/">
          <i class="fas fa-fw fa-home"></i>
          <span>Главная</span>
        </a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/video">
          <i class="fas fa-fw fa-video"></i>
          <span>Видеоролики</span>
        </a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/upload">
          <i class="fas fa-fw fa-cloud-upload-alt"></i>
          <span>Загрузить видео</span>
        </a>
      </li>
    </ul>
    <div id="content-wrapper">
      <router-view/>
      <!-- /.container-fluid -->
      <!-- Sticky Footer -->
    </div>
    <!-- /.content-wrapper -->
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import { useStore } from 'vuex';

@Options({
  components: {},
})
export default class MainLayout extends Vue {
  userName = '';

  store = useStore();

  logout(): void {
    this.store.commit('clearUser');
    this.$router.push('/login');
  }

  mounted(): void {
    if (!this.store.state.userId) {
      this.$router.push('/login');
    }
    this.userName = this.store.state.userName;
  }
}
</script>
