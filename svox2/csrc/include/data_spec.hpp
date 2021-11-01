// Copyright 2021 Alex Yu
#pragma once
#include "util.hpp"
#include <torch/extension.h>

using torch::Tensor;

enum BasisType {
  // For svox 1 compatibility
  // BASIS_TYPE_RGBA = 0
  BASIS_TYPE_SH = 1,
  // BASIS_TYPE_SG = 2
  // BASIS_TYPE_ASG = 3
  BASIS_TYPE_3D_TEXTURE = 4,
  BASIS_TYPE_MLP = 255,
};

struct SparseGridSpec {
  Tensor density_data;
  Tensor sh_data;
  Tensor links;
  Tensor _offset;
  Tensor _scaling;

  int basis_dim;
  uint8_t basis_type;
  Tensor basis_data;

  inline void check() {
    CHECK_INPUT(density_data);
    CHECK_INPUT(sh_data);
    CHECK_INPUT(links);
    CHECK_INPUT(basis_data);
    CHECK_CPU_INPUT(_offset);
    CHECK_CPU_INPUT(_scaling);
    TORCH_CHECK(density_data.is_floating_point());
    TORCH_CHECK(sh_data.is_floating_point());
    TORCH_CHECK(!links.is_floating_point());
    TORCH_CHECK(basis_data.is_floating_point());
    TORCH_CHECK(_offset.is_floating_point());
    TORCH_CHECK(_scaling.is_floating_point());
    TORCH_CHECK(density_data.ndimension() == 2);
    TORCH_CHECK(sh_data.ndimension() == 2);
    TORCH_CHECK(links.ndimension() == 3);
  }
};

struct CameraSpec {
  torch::Tensor c2w;
  float fx;
  float fy;
  float cx;
  float cy;
  int width;
  int height;

  float ndc_coeffx;
  float ndc_coeffy;

  inline void check() {
    CHECK_INPUT(c2w);
    TORCH_CHECK(c2w.is_floating_point());
    TORCH_CHECK(c2w.ndimension() == 2);
    TORCH_CHECK(c2w.size(1) == 4);
  }
};

struct RaysSpec {
  Tensor origins;
  Tensor dirs;
  inline void check() {
    CHECK_INPUT(origins);
    CHECK_INPUT(dirs);
    TORCH_CHECK(origins.is_floating_point());
    TORCH_CHECK(dirs.is_floating_point());
  }
};

struct RenderOptions {
  float background_brightness;
  // float step_epsilon;
  float step_size;
  float sigma_thresh;
  float stop_thresh;

  bool last_sample_opaque;

  // bool randomize;
  // uint32_t _m1, _m2, _m3;
};
