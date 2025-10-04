(function () {
  const toast = document.getElementById("toast-component");
  const titleEl = document.getElementById("toast-title");
  const msgEl = document.getElementById("toast-message");

  if (!toast || !titleEl || !msgEl) return;

  function resetStyle() {
    toast.classList.remove(
      "bg-green-50","border-green-500","text-green-700",
      "bg-red-50","border-red-500","text-red-700",
      "bg-white","border-gray-300","text-gray-800"
    );
  }


  // type: "success" | "error" | (default) "normal"
  window.showToast = function (title, message, type = "normal", duration = 8000) {
    resetStyle();

    if (type === "success") {
      toast.classList.add("bg-green-50","border-green-500","text-green-700");
    } else if (type === "error") {
      toast.classList.add("bg-red-50","border-red-500","text-red-700");
    } else {
      toast.classList.add("bg-white","border-gray-300","text-gray-800");
    }

    titleEl.textContent = title || "";
    msgEl.textContent = message || "";

    // show (kanan-bawah)
    toast.style.opacity = "1";
    toast.style.transform = "translateY(0)";

    clearTimeout(window.__kkToastTimer);
    window.__kkToastTimer = setTimeout(() => {
      toast.style.opacity = "0";
      toast.style.transform = "translateY(4rem)";
    }, duration);
  };
})();
