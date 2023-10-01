$(document).ready(function () {
  $(".like_btn").click(function () {
    let categoryId;
    categoryId = $(this).attr("data-categoryid");

    $.get("/dive/like_category/", { category_id: categoryId }, function (data) {
      let like_countId = "#like_count".concat(categoryId);
      let like_btn = `button[data-categoryid="${categoryId}"]`;
      let span_icon = like_btn + " " + "svg";
      if (data["is_liked"]) {
        $(like_btn).css("color", "#0d6efd");
        $(span_icon).replaceWith(feather.icons["thumbs-up"].toSvg());
      } else {
        $(like_btn).css("color", "green");
        $(span_icon).replaceWith(feather.icons["check-circle"].toSvg());
      }
      $(like_countId).html(data["likes"]);
    });
  });
});
