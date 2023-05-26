/********************************************************************************
 * Copyright (C) 2017-2020 German Aerospace Center (DLR). 
 * Eclipse ADORe, Automated Driving Open Research https://eclipse.org/adore
 *
 * This program and the accompanying materials are made available under the 
 * terms of the Eclipse Public License 2.0 which is available at
 * http://www.eclipse.org/legal/epl-2.0.
 *
 * SPDX-License-Identifier: EPL-2.0 
 *
 * Contributors: 
 *   Jan Lauermann - initial API and implementation
 ********************************************************************************/

#pragma once

#include <ros/ros.h>
#include <adore_if_ros/ros_com_patterns.h>
#include <adore/params/ap_lane_change_view.h>

namespace adore
{
  namespace if_ROS
  {
    namespace params
    {
      class PLaneChangeView:public adore::params::APLaneChangeView,ROSParam
      {
        public:
        PLaneChangeView(ros::NodeHandle n,std::string prefix)
        :ROSParam(n,prefix + "lane_change_view/")
        {
        }
        virtual double getLookAhead()const override
        {
          double value = 150.0;
          static const std::string name = prefix_ + "look_ahead";
          get(name,value);
          return value;
        }
		    virtual double getLookBehind()const override
        {
          double value = 5.0;
          static const std::string name = prefix_ + "look_behind";
          get(name,value);
          return value;
        }
        virtual double getMaximumNavCostLoss() const override
        {
          double value = 1000.0;
          static const std::string name = prefix_ + "maximum_navcost_loss";
          get(name,value);
          return value;
        }
		    virtual double getBaselineFitSmoothness()const override
        {
          double value = 0.05;
          static const std::string name = prefix_ + "baseline_fit_smoothness";
          get(name,value);
          return value;
        }
      };
    }
  }
}