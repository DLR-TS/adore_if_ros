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
 *   Reza Dariani - initial API and implementation
 *   Anas Abulehia
 ********************************************************************************/


#include <adore_if_ros_scheduling/baseapp.h>
#include <adore_if_ros/factorycollection.h>
#include <adore/apps/lqr_platoon_controller.h>

namespace adore
{
    namespace if_ROS
    {
        class LQRPlatoonNode : public FactoryCollection, public adore_if_ros_scheduling::Baseapp
        {
        public:
            adore::apps::LQRPlatoonController *controller_;
            LQRPlatoonNode() {}
            void init(int argc, char **argv, double rate, std::string nodename)
            {
                Baseapp::init(argc, argv, rate, nodename);
                Baseapp::initSim();
                FactoryCollection::init(getRosNodeHandle());
                controller_ = new adore::apps::GapProvider();

                // timer callbacks
                std::function<void()> run_fcn(std::bind(&adore::apps::GapProvider::update, controller_));
                Baseapp::addTimerCallback(run_fcn);
            }
        };
    } // namespace if_ROS
} // namespace adore

int main(int argc, char **argv)
{
    auto node = new adore::if_ROS::LQRPlatoonNode();
    node->init(argc, argv, 10.0, "gap_provider");   
    node->run();
    return 0;
}