(() => {
  "use strict";

  const toggle = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".nav-links");

  if (toggle && nav) {
    const closeMenu = () => {
      nav.classList.remove("open");
      toggle.setAttribute("aria-expanded", "false");
    };

    toggle.addEventListener("click", () => {
      const open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(open));
    });

    nav.querySelectorAll("a").forEach((link) => link.addEventListener("click", closeMenu));
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") closeMenu();
    });
    document.addEventListener("click", (event) => {
      if (!nav.contains(event.target) && !toggle.contains(event.target)) closeMenu();
    });
  }

  const currentPage = window.location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav-links a").forEach((link) => {
    const href = link.getAttribute("href") || "";
    const page = href.split("#")[0] || "index.html";
    if (page === currentPage && !href.includes("#")) {
      link.setAttribute("aria-current", "page");
    }
  });

  const form = document.querySelector("#early-access-form");
  if (form) {
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      if (!form.reportValidity()) return;

      const data = new FormData(form);
      const value = (key) => String(data.get(key) || "").trim();
      const organisation = value("organisation");
      const subject = encodeURIComponent("Zivas institutional demo request — " + organisation);
      const body = encodeURIComponent([
        "Hello Zivas team,",
        "",
        "I would like to request a guided Zivas demonstration.",
        "",
        "Name: " + value("name"),
        "Work email: " + value("email"),
        "Role: " + value("role"),
        "Institution: " + organisation,
        "Country/region: " + value("region"),
        "Learner population: " + (value("population") || "Not provided"),
        "What I would like to explore: " + (value("goals") || "Not provided"),
        ""
      ].join("\n"));

      const status = form.querySelector('[role="status"]');
      if (status) {
        status.textContent = "Your email application is opening with the request prepared. Review it and press Send to complete your enquiry.";
      }
      window.location.href = "mailto:support.zivas@gmail.com?subject=" + subject + "&body=" + body;
    });
  }
})();