<script>
</script>



<div>

    <div class="custom-wrapper pure-g" id="menu">
      <div class="pure-u-1 pure-u-md-1-3">
        <div class="pure-menu">
          <a href="#" class="pure-menu-heading custom-brand">Brand</a>
          <a href="#" class="custom-toggle" id="toggle">
            <s class="bar"></s> <s class="bar"></s>
          </a>
        </div>
      </div>
      <div class="pure-u-1 pure-u-md-1-3">
        <div class="pure-menu pure-menu-horizontal custom-can-transform">
          <ul class="pure-menu-list">
            <li class="pure-menu-item">
              <a href="/" class="pure-menu-link">Home</a>
            </li>
            <li class="pure-menu-item">
              <a href="/about" class="pure-menu-link">About</a>
            </li>
            <li class="pure-menu-item">
              <a href="/about2" class="pure-menu-link">About 2</a>
            </li>
            <li class="pure-menu-item">
              <a href="/contact" class="pure-menu-link">Contact</a>
            </li>
          </ul>
        </div>
      </div>
      <div class="pure-u-1 pure-u-md-1-3">
        <div class="pure-menu pure-menu-horizontal custom-menu-3 custom-can-transform">
          <ul class="pure-menu-list">
            <li class="pure-menu-item">
              <a href="#" class="pure-menu-link">Yahoo</a>
            </li>
            <li class="pure-menu-item">
              <a href="#" class="pure-menu-link">W3C</a>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <div id="layout" class=" active-left active-right">
      <!-- Menu toggle -->
      <a href="#menu-left" id="menu-left-link" class="menu-left-link active-left">
        <i id="menu-left-link-icon" class="icss-caret-square-l" style="font-size:2em; color:white"></i>
      </a>

      <div id="menu-left" class=" active-left" >
        <slot name="left-menu-content"/>
      </div>

      <div>
        <slot name="main-block-content"/>
      </div>

      <a id="menu-right-link" class="menu-right-link active-right">
        <i id="menu-right-link-icon" class="icss-caret-square-r" style="font-size:2em; color:white"></i>
      </a>
      <div id="menu-right" class=" active-right">
        <slot name="right-menu-content"/>
      </div>

    </div>




    <div class="footer l-box is-center">
      Made with love.
    </div>

</div>

