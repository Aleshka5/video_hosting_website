<template>
  <div class="container-fluid pb-0">
    <div class="video-block section-padding">
      <div class="row">
          <div class="col-md-8">
            <div class="single-video-left">
                <div class="single-video">
                  <VideoPlayer :options="videoOptions" />
                </div>
                <div class="single-video-title box mb-3">
                  <h2><a href="#">Contrary to popular belief, Lorem Ipsum (2019) is not.</a></h2>
                  <p class="mb-0"><i class="fas fa-eye"></i> 2,729,347 views</p>
                </div>
                <div class="single-video-author box mb-3">
                  <div class="float-right"><button class="btn btn-danger" type="button">Subscribe <strong>1.4M</strong></button> <button class="btn btn btn-outline-danger" type="button"><i class="fas fa-bell"></i></button></div>
                  <img class="img-fluid" src="@/assets/img/s4.png" alt="">
                  <p><a href="#"><strong>Osahan Channel</strong></a> <span title="" data-placement="top" data-toggle="tooltip" data-original-title="Verified"><i class="fas fa-check-circle text-success"></i></span></p>
                  <small>Published on Aug 10, 2018</small>
                </div>
                <div class="single-video-info-content box mb-3">
                  <h6>Cast:</h6>
                  <p>Nathan Drake , Victor Sullivan , Sam Drake , Elena Fisher</p>
                  <h6>Category :</h6>
                  <p>Gaming , PS4 Exclusive , Gameplay , 1080p</p>
                  <h6>About :</h6>
                  <p>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved overVarious versions have evolved over the years, sometimes </p>
                  <h6>Tags :</h6>
                  <p class="tags mb-0">
                      <span><a href="#">Uncharted 4</a></span>
                      <span><a href="#">Playstation 4</a></span>
                      <span><a href="#">Gameplay</a></span>
                      <span><a href="#">1080P</a></span>
                      <span><a href="#">ps4Share</a></span>
                      <span><a href="#">+ 6</a></span>
                  </p>
                </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="single-video-right">
                <div class="row">
                  <div class="col-md-12">
                      <div class="adblock">
                        <div class="img">
                            Google AdSense<br>
                            336 x 280
                        </div>
                      </div>
                      <div class="main-title">
                        <div class="btn-group float-right right-action">
                            <a href="#" class="right-action-link text-gray" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Sort by <i class="fa fa-caret-down" aria-hidden="true"></i>
                            </a>
                            <div class="dropdown-menu dropdown-menu-right">
                              <a class="dropdown-item" href="#"><i class="fas fa-fw fa-star"></i> &nbsp; Top Rated</a>
                              <a class="dropdown-item" href="#"><i class="fas fa-fw fa-signal"></i> &nbsp; Viewed</a>
                              <a class="dropdown-item" href="#"><i class="fas fa-fw fa-times-circle"></i> &nbsp; Close</a>
                            </div>
                        </div>
                        <h6>Up Next</h6>
                      </div>
                  </div>
                  <div class="col-md-12">
                      <div class="video-card video-card-list">
                        <div class="video-card-image">
                            <a class="play-icon" href="#"><i class="fas fa-play-circle"></i></a>
                            <a href="#"><img class="img-fluid" src="@/assets/img/v1.png" alt=""></a>
                            <div class="time">3:50</div>
                        </div>
                        <div class="video-card-body">
                            <div class="btn-group float-right right-action">
                              <a href="#" class="right-action-link text-gray" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                              <i class="fa fa-ellipsis-v" aria-hidden="true"></i>
                              </a>
                              <div class="dropdown-menu dropdown-menu-right">
                                  <a class="dropdown-item" href="#"><i class="fas fa-fw fa-star"></i> &nbsp; Top Rated</a>
                                  <a class="dropdown-item" href="#"><i class="fas fa-fw fa-signal"></i> &nbsp; Viewed</a>
                                  <a class="dropdown-item" href="#"><i class="fas fa-fw fa-times-circle"></i> &nbsp; Close</a>
                              </div>
                            </div>
                            <div class="video-title">
                              <a href="#">Here are many variati of passages of Lorem</a>
                            </div>
                            <div class="video-page text-success">
                              Education  <a title="" data-placement="top" data-toggle="tooltip" href="#" data-original-title="Verified"><i class="fas fa-check-circle text-success"></i></a>
                            </div>
                            <div class="video-view">
                              1.8M views &nbsp;<i class="fas fa-calendar-alt"></i> 11 Months ago
                            </div>
                        </div>
                      </div>
                      <div class="video-card video-card-list">
                        <div class="video-card-image">
                            <a class="play-icon" href="#"><i class="fas fa-play-circle"></i></a>
                            <a href="#"><img class="img-fluid" src="@/assets/img/v2.png" alt=""></a>
                            <div class="time">3:50</div>
                        </div>
                        <div class="video-card-body">
                            <div class="btn-group float-right right-action">
                              <a href="#" class="right-action-link text-gray" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                              <i class="fa fa-ellipsis-v" aria-hidden="true"></i>
                              </a>
                              <div class="dropdown-menu dropdown-menu-right">
                                  <a class="dropdown-item" href="#"><i class="fas fa-fw fa-star"></i> &nbsp; Top Rated</a>
                                  <a class="dropdown-item" href="#"><i class="fas fa-fw fa-signal"></i> &nbsp; Viewed</a>
                                  <a class="dropdown-item" href="#"><i class="fas fa-fw fa-times-circle"></i> &nbsp; Close</a>
                              </div>
                            </div>
                            <div class="video-title">
                              <a href="#">Duis aute irure dolor in reprehenderit in.</a>
                            </div>
                            <div class="video-page text-success">
                              Education  <a title="" data-placement="top" data-toggle="tooltip" href="#" data-original-title="Verified"><i class="fas fa-check-circle text-success"></i></a>
                            </div>
                            <div class="video-view">
                              1.8M views &nbsp;<i class="fas fa-calendar-alt"></i> 11 Months ago
                            </div>
                        </div>
                      </div>
                      <div class="video-card video-card-list">
                        <div class="video-card-image">
                            <a class="play-icon" href="#"><i class="fas fa-play-circle"></i></a>
                            <a href="#"><img class="img-fluid" src="@/assets/img/v3.png" alt=""></a>
                            <div class="time">3:50</div>
                        </div>
                        <div class="video-card-body">
                            <div class="btn-group float-right right-action">
                              <a href="#" class="right-action-link text-gray" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                              <i class="fa fa-ellipsis-v" aria-hidden="true"></i>
                              </a>
                              <div class="dropdown-menu dropdown-menu-right">
                                  <a class="dropdown-item" href="#"><i class="fas fa-fw fa-star"></i> &nbsp; Top Rated</a>
                                  <a class="dropdown-item" href="#"><i class="fas fa-fw fa-signal"></i> &nbsp; Viewed</a>
                                  <a class="dropdown-item" href="#"><i class="fas fa-fw fa-times-circle"></i> &nbsp; Close</a>
                              </div>
                            </div>
                            <div class="video-title">
                              <a href="#">Culpa qui officia deserunt mollit anim</a>
                            </div>
                            <div class="video-page text-success">
                              Education  <a title="" data-placement="top" data-toggle="tooltip" href="#" data-original-title="Verified"><i class="fas fa-check-circle text-success"></i></a>
                            </div>
                            <div class="video-view">
                              1.8M views &nbsp;<i class="fas fa-calendar-alt"></i> 11 Months ago
                            </div>
                        </div>
                      </div>
                      <div class="video-card video-card-list">
                        <div class="video-card-image">
                            <a class="play-icon" href="#"><i class="fas fa-play-circle"></i></a>
                            <a href="#"><img class="img-fluid" src="@/assets/img/v4.png" alt=""></a>
                            <div class="time">3:50</div>
                        </div>
                        <div class="video-card-body">
                            <div class="btn-group float-right right-action">
                              <a href="#" class="right-action-link text-gray" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                              <i class="fa fa-ellipsis-v" aria-hidden="true"></i>
                              </a>
                              <div class="dropdown-menu dropdown-menu-right">
                                  <a class="dropdown-item" href="#"><i class="fas fa-fw fa-star"></i> &nbsp; Top Rated</a>
                                  <a class="dropdown-item" href="#"><i class="fas fa-fw fa-signal"></i> &nbsp; Viewed</a>
                                  <a class="dropdown-item" href="#"><i class="fas fa-fw fa-times-circle"></i> &nbsp; Close</a>
                              </div>
                            </div>
                            <div class="video-title">
                              <a href="#">Deserunt mollit anim id est laborum.</a>
                            </div>
                            <div class="video-page text-success">
                              Education  <a title="" data-placement="top" data-toggle="tooltip" href="#" data-original-title="Verified"><i class="fas fa-check-circle text-success"></i></a>
                            </div>
                            <div class="video-view">
                              1.8M views &nbsp;<i class="fas fa-calendar-alt"></i> 11 Months ago
                            </div>
                        </div>
                      </div>
                      <div class="video-card video-card-list">
                        <div class="video-card-image">
                            <a class="play-icon" href="#"><i class="fas fa-play-circle"></i></a>
                            <a href="#"><img class="img-fluid" src="@/assets/img/v5.png" alt=""></a>
                            <div class="time">3:50</div>
                        </div>
                        <div class="video-card-body">
                            <div class="btn-group float-right right-action">
                              <a href="#" class="right-action-link text-gray" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                              <i class="fa fa-ellipsis-v" aria-hidden="true"></i>
                              </a>
                              <div class="dropdown-menu dropdown-menu-right">
                                  <a class="dropdown-item" href="#"><i class="fas fa-fw fa-star"></i> &nbsp; Top Rated</a>
                                  <a class="dropdown-item" href="#"><i class="fas fa-fw fa-signal"></i> &nbsp; Viewed</a>
                                  <a class="dropdown-item" href="#"><i class="fas fa-fw fa-times-circle"></i> &nbsp; Close</a>
                              </div>
                            </div>
                            <div class="video-title">
                              <a href="#">Exercitation ullamco laboris nisi ut.</a>
                            </div>
                            <div class="video-page text-success">
                              Education  <a title="" data-placement="top" data-toggle="tooltip" href="#" data-original-title="Verified"><i class="fas fa-check-circle text-success"></i></a>
                            </div>
                            <div class="video-view">
                              1.8M views &nbsp;<i class="fas fa-calendar-alt"></i> 11 Months ago
                            </div>
                        </div>
                      </div>
                      <div class="video-card video-card-list">
                        <div class="video-card-image">
                            <a class="play-icon" href="#"><i class="fas fa-play-circle"></i></a>
                            <a href="#"><img class="img-fluid" src="@/assets/img/v6.png" alt=""></a>
                            <div class="time">3:50</div>
                        </div>
                        <div class="video-card-body">
                            <div class="btn-group float-right right-action">
                              <a href="#" class="right-action-link text-gray" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                              <i class="fa fa-ellipsis-v" aria-hidden="true"></i>
                              </a>
                              <div class="dropdown-menu dropdown-menu-right">
                                  <a class="dropdown-item" href="#"><i class="fas fa-fw fa-star"></i> &nbsp; Top Rated</a>
                                  <a class="dropdown-item" href="#"><i class="fas fa-fw fa-signal"></i> &nbsp; Viewed</a>
                                  <a class="dropdown-item" href="#"><i class="fas fa-fw fa-times-circle"></i> &nbsp; Close</a>
                              </div>
                            </div>
                            <div class="video-title">
                              <a href="#">There are many variations of passages of Lorem</a>
                            </div>
                            <div class="video-page text-success">
                              Education  <a title="" data-placement="top" data-toggle="tooltip" href="#" data-original-title="Verified"><i class="fas fa-check-circle text-success"></i></a>
                            </div>
                            <div class="video-view">
                              1.8M views &nbsp;<i class="fas fa-calendar-alt"></i> 11 Months ago
                            </div>
                        </div>
                      </div>
                      <div class="adblock mt-0">
                        <div class="img">
                            Google AdSense<br>
                            336 x 280
                        </div>
                      </div>
                      <div class="video-card video-card-list">
                        <div class="video-card-image">
                            <a class="play-icon" href="#"><i class="fas fa-play-circle"></i></a>
                            <a href="#"><img class="img-fluid" src="@/assets/img/v2.png" alt=""></a>
                            <div class="time">3:50</div>
                        </div>
                        <div class="video-card-body">
                            <div class="btn-group float-right right-action">
                              <a href="#" class="right-action-link text-gray" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                              <i class="fa fa-ellipsis-v" aria-hidden="true"></i>
                              </a>
                              <div class="dropdown-menu dropdown-menu-right">
                                  <a class="dropdown-item" href="#"><i class="fas fa-fw fa-star"></i> &nbsp; Top Rated</a>
                                  <a class="dropdown-item" href="#"><i class="fas fa-fw fa-signal"></i> &nbsp; Viewed</a>
                                  <a class="dropdown-item" href="#"><i class="fas fa-fw fa-times-circle"></i> &nbsp; Close</a>
                              </div>
                            </div>
                            <div class="video-title">
                              <a href="#">Duis aute irure dolor in reprehenderit in.</a>
                            </div>
                            <div class="video-page text-success">
                              Education  <a title="" data-placement="top" data-toggle="tooltip" href="#" data-original-title="Verified"><i class="fas fa-check-circle text-success"></i></a>
                            </div>
                            <div class="video-view">
                              1.8M views &nbsp;<i class="fas fa-calendar-alt"></i> 11 Months ago
                            </div>
                        </div>
                      </div>
                  </div>
                </div>
            </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import VideoPlayer from '@/components/VideoPlayer.vue';

// import '@/assets/video/kamila.mp4';

@Options({
  components: {
    VideoPlayer,
  },
})
export default class VideoView extends Vue {
  videoOptions = {
    autoplay: false,
    controls: true,
  }
}
</script>
