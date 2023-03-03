<template>
  <nav class="navbar navbar-expand navbar-light bg-white static-top osahan-nav sticky-top">
      &nbsp;&nbsp; 
      <button class="btn btn-link btn-sm text-secondary order-1 order-sm-0" id="sidebarToggle">
      <i class="fas fa-bars"></i>
      </button> &nbsp;&nbsp;
      <a class="navbar-brand mr-1" href="index.html"><img class="img-fluid" alt="" src="img/logo.png"></a>
      <!-- Navbar Search -->
      <form class="d-none d-md-inline-block form-inline ml-auto mr-0 mr-md-5 my-2 my-md-0 osahan-navbar-search">
        <div class="input-group">
            <input type="text" class="form-control" placeholder="Search for...">
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
            <a class="nav-link" href="upload.html">
            <i class="fas fa-plus-circle fa-fw"></i>
            Upload Video
            </a>
        </li>
        <li class="nav-item dropdown no-arrow mx-1">
            <a class="nav-link dropdown-toggle" href="#" id="alertsDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <i class="fas fa-bell fa-fw"></i>
            <span class="badge badge-danger">9+</span>
            </a>
            <div class="dropdown-menu dropdown-menu-right" aria-labelledby="alertsDropdown">
              <a class="dropdown-item" href="#"><i class="fas fa-fw fa-edit "></i> &nbsp; Action</a>
              <a class="dropdown-item" href="#"><i class="fas fa-fw fa-headphones-alt "></i> &nbsp; Another action</a>
              <div class="dropdown-divider"></div>
              <a class="dropdown-item" href="#"><i class="fas fa-fw fa-star "></i> &nbsp; Something else here</a>
            </div>
        </li>
        <li class="nav-item dropdown no-arrow mx-1">
            <a class="nav-link dropdown-toggle" href="#" id="messagesDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <i class="fas fa-envelope fa-fw"></i>
            <span class="badge badge-success">7</span>
            </a>
            <div class="dropdown-menu dropdown-menu-right" aria-labelledby="messagesDropdown">
              <a class="dropdown-item" href="#"><i class="fas fa-fw fa-edit "></i> &nbsp; Action</a>
              <a class="dropdown-item" href="#"><i class="fas fa-fw fa-headphones-alt "></i> &nbsp; Another action</a>
              <div class="dropdown-divider"></div>
              <a class="dropdown-item" href="#"><i class="fas fa-fw fa-star "></i> &nbsp; Something else here</a>
            </div>
        </li>
        <li class="nav-item dropdown no-arrow osahan-right-navbar-user">
            <a class="nav-link dropdown-toggle user-dropdown-link" href="#" id="userDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <img alt="Avatar" src="img/user.png">
            Osahan 
            </a>
            <div class="dropdown-menu dropdown-menu-right" aria-labelledby="userDropdown">
              <a class="dropdown-item" href="account.html"><i class="fas fa-fw fa-user-circle"></i> &nbsp; My Account</a>
              <a class="dropdown-item" href="subscriptions.html"><i class="fas fa-fw fa-video"></i> &nbsp; Subscriptions</a>
              <a class="dropdown-item" href="settings.html"><i class="fas fa-fw fa-cog"></i> &nbsp; Settings</a>
              <div class="dropdown-divider"></div>
              <a class="dropdown-item" href="#" data-toggle="modal" data-target="#logoutModal"><i class="fas fa-fw fa-sign-out-alt"></i> &nbsp; Logout</a>
            </div>
        </li>
      </ul>
  </nav>
  <div id="wrapper">
    <!-- Sidebar -->
    <ul class="sidebar navbar-nav">
      <li class="nav-item active">
          <a class="nav-link" href="/">
          <i class="fas fa-fw fa-home"></i>
          <span>Home</span>
          </a>
      </li>
      <li class="nav-item">
          <a class="nav-link" href="channels.html">
          <i class="fas fa-fw fa-users"></i>
          <span>Channels</span>
          </a>
      </li>
      <li class="nav-item">
          <a class="nav-link" href="single-channel.html">
          <i class="fas fa-fw fa-user-alt"></i>
          <span>Single Channel</span>
          </a>
      </li>
      <li class="nav-item">
          <a class="nav-link" href="/video">
          <i class="fas fa-fw fa-video"></i>
          <span>Video Page</span>
          </a>
      </li>
      <li class="nav-item">
          <a class="nav-link" href="upload-video.html">
          <i class="fas fa-fw fa-cloud-upload-alt"></i>
          <span>Upload Video</span>
          </a>
      </li>
      <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <i class="fas fa-fw fa-folder"></i>
          <span>Pages</span>
          </a>
          <div class="dropdown-menu">
            <h6 class="dropdown-header">Login Screens:</h6>
            <a class="dropdown-item" href="login.html">Login</a>
            <a class="dropdown-item" href="register.html">Register</a>
            <a class="dropdown-item" href="forgot-password.html">Forgot Password</a>
            <div class="dropdown-divider"></div>
            <h6 class="dropdown-header">Other Pages:</h6>
            <a class="dropdown-item" href="404.html">404 Page</a>
            <a class="dropdown-item" href="blank.html">Blank Page</a>
          </div>
      </li>
      <li class="nav-item">
          <a class="nav-link" href="history-page.html">
          <i class="fas fa-fw fa-history"></i>
          <span>History Page</span>
          </a>
      </li>
      <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="categories.html" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <i class="fas fa-fw fa-list-alt"></i>
          <span>Categories</span>
          </a>
          <div class="dropdown-menu">
            <a class="dropdown-item" href="categories.html">Movie</a>
            <a class="dropdown-item" href="categories.html">Music</a>
            <a class="dropdown-item" href="categories.html">Television</a>
          </div>
      </li>
      <li class="nav-item channel-sidebar-list">
          <h6>SUBSCRIPTIONS</h6>
          <ul>
            <li>
                <a href="subscriptions.html">
                <img class="img-fluid" alt="" src="img/s1.png"> Your Life 
                </a>
            </li>
            <li>
                <a href="subscriptions.html">
                <img class="img-fluid" alt="" src="img/s2.png"> Unboxing  <span class="badge badge-warning">2</span>
                </a>
            </li>
            <li>
                <a href="subscriptions.html">
                <img class="img-fluid" alt="" src="img/s3.png"> Product / Service  
                </a>
            </li>
            <li>
                <a href="subscriptions.html">
                <img class="img-fluid" alt="" src="img/s4.png">  Gaming 
                </a>
            </li>
          </ul>
      </li>
    </ul>
    <div id="content-wrapper">
      <router-view/>
      <!-- /.container-fluid -->
      <!-- Sticky Footer -->
      <footer class="sticky-footer">
        <div class="container">
          <div class="row no-gutters">
              <div class="col-lg-6 col-sm-6">
                <p class="mt-1 mb-0"><strong class="text-dark">Vidoe</strong>. 
                  <small class="mt-0 mb-0"><a class="text-primary" target="_blank" href="https://www.templatespoint.net/">Templates Point</a>
                  </small>
                </p>
              </div>
              <div class="col-lg-6 col-sm-6 text-right">
                <div class="app">
                  <a href="#"><img alt="" src="img/google.png"></a>
                  <a href="#"><img alt="" src="img/apple.png"></a>
                </div>
              </div>
          </div>
        </div>
      </footer>
    </div>
    <!-- /.content-wrapper -->
  </div>
  <!-- <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav> -->
</template>

<style lang="scss">
</style>
